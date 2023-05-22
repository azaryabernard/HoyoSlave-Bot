import aiohttp
import io
import pandas as pd
from discord import Embed
from .models import (
    Character, Element, Path, 
    CHARACTERS,
    get_element_url, gen_character_dict,
    save_dict_to_json, load_json_to_dict
)


""" HELPER FUNCTIONS """
# This function is used to get the character by name
def get_character_by_name(name: str):
    for character in CHARACTERS:
        if name.strip().lower() in character.get_name().lower():
            return character
    return None

# This function is used to get the character by element (unused)
def get_characters_by_element(element: Element):
    characters = []
    for character in CHARACTERS:
        if element == character.get_element():
            characters.append(character)
    return characters

# This function is used to get the character by rarity (unused)
def get_characters_by_rarity(rarity: int):
    characters = []
    for character in CHARACTERS:
        if rarity == character.get_rarity():
            characters.append(character)
    return characters

# This function is used to get the character by Path (unused)
def get_characters_by_path(path: Path):
    characters = []
    for character in CHARACTERS:
        if path == character.path():
            characters.append(character)
    return characters

# This function is used to prettify the seperation of fields by roles
def seperate_by_roles(strs: list[str], roles_count: int):
    # remove NaN
    strs = [s for s in strs if str(s) != 'nan']
    # seperate by roles
    if len(strs) == roles_count:
        return [f"**[Role {i+1}]**\n{r}" for i, r in enumerate(strs)]
    elif strs:
        return [f"**[All]**\n" + strs[0]]
    else:
        return []

# This function is used to fetch the data from the URL asynchronously
async def fetch(session, url):
    async with session.get(url) as response:
        if response.status != 200:
           print(f"Error getting data from {url}")
           return None
        response.encoding = 'utf-8'
        return await response.text()


""" MAIN FUNCTIONS """
# This function is used to get the data from google sheets
async def get_data_from_google_sheets(character: Character, cached: bool = True) -> dict[str, any]:
    char_dict = None
    # Checking if the data is cached
    if cached:
        char_dict = await load_json_to_dict(character)
        if char_dict is None:
            print("There is no cached data for this character. Fetching from google docs.")
            cached = False
        elif not char_dict["roles"] or not char_dict["light_cones"] or not char_dict["relics"]:
            print("Cached data incomplete / corrupted. Fetching from google docs.")
            cached = False
        else:
            print("Fetching from cache.")
    # If it is not cached, fetch from the google docs from Genshin Impact Helper's Team
    if not cached:
        # URL for the google docs
        url = get_element_url(character.get_element())
        print(f"Fetching from {url}")
        # Getting the data from the URL
        response = None
        async with aiohttp.ClientSession() as session:
            response = await fetch(session, url)
        # Converting the data to a dataframe
        df = pd.read_csv(io.StringIO(response), sep=',', engine='python')
        df = df.drop(df.columns[[0]], axis=1)[4:]
        df.columns = ['characters', 'roles', 'light_cones', 'relics', 'main_stats', 'sub_stats', 'traces', 'tips']
        df.reset_index(drop=True, inplace=True)
        # special case for traveler
        if "Trailblazer" in character.get_name():
            character = Character(
                "Trailblazer" + f" ({character.get_element().name.capitalize()})", 
                character.get_element(), 
                character.get_rarity(), 
                character.get_path()
            )
        # Parse characters data with character name
        df_bool = df.characters.apply(
            lambda x: character.get_first_name().lower() in x.lower() and character.get_last_name().lower() in x.lower()
            if isinstance(x, str) else False
        )
        start_index = df_bool.eq(True).argmax()
        end_index = df.characters[start_index+1:].notna().idxmax()
        # parse to Dict
        char_dict = gen_character_dict(
            character=character,
            roles=df.roles[start_index+2:end_index].tolist(),
            light_cones=df.light_cones[start_index+2:end_index].tolist(),
            relics=df.relics[start_index+2:end_index].tolist(),
            main_stats=df.main_stats[start_index+2:end_index].tolist(),
            sub_stats=df.sub_stats[start_index+2:end_index].tolist(),
            traces=df.traces[start_index+2:end_index].tolist(),
            tips=df.tips[start_index+2:end_index].tolist(),
            notes=df.roles[end_index]
        )
        # Saving the data to cache
        await save_dict_to_json(char_dict)
    # Returning the data
    return char_dict


# Exported function to get the character build, may return None
async def get_character_build(name: str, cached: bool = True) -> list[Embed]:
    # Getting the character by name
    character = get_character_by_name(name)
    if character == None:
        print(f"Character not found with name: {name}")
        return None
    # Getting the data from google sheets / cache
    char_dict = await get_data_from_google_sheets(character, cached)
    if char_dict is None:
        print(f"Error getting data for character: {character.get_name()}")
        return None
    # Creating the Embed object for discord
    # Roles
    roles_count = len(char_dict["roles"])

    # Main Embed (Roles, Light Cones, Relics)
    main_embed = Embed(
            title=f"{character.get_name()} (1/4)", 
            description=character.get_description(),
        ).set_thumbnail(url="attachment://image.png")
    
    roles = seperate_by_roles(char_dict["roles"], roles_count)
    light_cones = seperate_by_roles(char_dict["light_cones"], roles_count)
    relics = seperate_by_roles(char_dict["relics"], roles_count)

    for i in range(roles_count):
        main_embed.add_field(
            name="Roles" if i == 0 else "",
            value=roles[i] if i < len(roles) else "",
            inline=True
        )
        main_embed.add_field(
            name="Light Cones" if i == 0 else "",
            value=light_cones[i] if i < len(light_cones) else "",
            inline=True
        )
        main_embed.add_field(
            name="Relics" if i == 0 else "",
            value=relics[i] if i < len(relics) else "",
            inline=True
        )
    # Stats Embed (Main Stats, Sub Stats)
    stats_embed = Embed(
            title=f"{character.get_name()} (2/4)",
            description=character.get_description(),
        ).set_thumbnail(url="attachment://image.png")
    
    main_stats = seperate_by_roles(char_dict["main_stats"], roles_count)
    sub_stats = seperate_by_roles(char_dict["sub_stats"], roles_count)
    traces = seperate_by_roles(char_dict["traces"], roles_count)

    for i in range(roles_count):
        stats_embed.add_field(
            name="Main Stats" if i == 0 else "",
            value=main_stats[i] if i < len(main_stats) else "",
            inline=True
        )
        stats_embed.add_field(
            name="Sub Stats" if i == 0 else "",
            value=sub_stats[i] if i < len(sub_stats) else "",
            inline=True
        )
        stats_embed.add_field(
            name="Trace Priority" if i == 0 else "",
            value=traces[i] if i < len(traces) else "",
            inline=True
        )
    # Tips Embed (long > 1024)
    tips_embed = Embed(
        title=f"{character.get_name()} (3/4)",
        description=character.get_description(),
    ).set_thumbnail(url="attachment://image.png")

    tips = seperate_by_roles(char_dict["tips"], roles_count)
    tips.append("...")
    for i, tip in enumerate(tips):
        tips_embed.add_field(
            name="Ability Priority (TBA)" if i == 0 else "",
            value=tip,
            inline=False
        )
    # Notes Embed (long > 1024)
    notes_embed = Embed(
        title=f"{character.get_name()} (4/4)",
        description=character.get_description(),
    ).set_thumbnail(
        url="attachment://image.png"
    ).set_footer(
        text= "Source: Honkai: Star Rail Community Character Build Guide"
    )
    notes = char_dict["notes"].split("\n\n")
    notes =  [[note[0:512], note[512:1024]] if len(note) >= 1024 else [note] for note in notes]
    notes = [note for subnotes in notes for note in subnotes]
    for i, note in enumerate(notes):
        notes_embed.add_field(
            name="Notes" if i == 0 else "",
            value=note,
            inline=False
        )
    # Returning the Embeds
    return (
        [main_embed, stats_embed, tips_embed, notes_embed],
        character.get_image_path()
    )