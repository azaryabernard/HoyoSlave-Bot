from enum import Enum
import os
import json


# The key for the google sheets
# Source: [Honkai: Star Rail Helper's Team](https://docs.google.com/spreadsheets/d/1FG_6viMaygymJucNU60pGptbgDjLNOpUKPD81pZQ1_Y)
SHEETS_KEY = "1FG_6viMaygymJucNU60pGptbgDjLNOpUKPD81pZQ1_Y"
SHEET_CHANGELOGS_ID = "172546500"
SHEET_QUANTUM_ID = "1169063456"
SHEET_FIRE_ID = "954718212"
SHEET_ICE_ID = "1354385732"
SHEET_LIGHTNING_ID = "408609723"
SHEET_WIND_ID = "653464458"
SHEET_IMAGINARY_ID = "1780570478"
SHEET_PHYSICAL_ID = "1836385190"

dirname = os.path.dirname(__file__)

# Enum for the elements
class Element(Enum):
    QUANTUM, FIRE, ICE, LIGHTNING, WIND, IMAGINARY, PHYSICAL = range(7)

    def get_sheet_id(self):
        if self == Element.QUANTUM:
            return SHEET_QUANTUM_ID
        elif self == Element.FIRE:
            return SHEET_FIRE_ID
        elif self == Element.ICE:
            return SHEET_ICE_ID
        elif self == Element.LIGHTNING:
            return SHEET_LIGHTNING_ID
        elif self == Element.WIND:
            return SHEET_WIND_ID
        elif self == Element.IMAGINARY:
            return SHEET_IMAGINARY_ID
        elif self == Element.PHYSICAL:
            return SHEET_PHYSICAL_ID
        
# Enum for the weapon types
class Path(Enum):
    HUNT, ABUNDANCE, DESTURCTION, ERUDITION, PRESERVATION, NIHILITY, HARMONY = range(7)

# Class for the characters
class Character():
    def __init__(self, name: str, element: Element, rarity: int, path: Path):
        self.name = name
        self.element = element
        self.rarity = rarity
        self.path = path

    def get_name(self):
        return self.name
    
    def get_first_name(self):
        return self.name.split(" ")[0]

    def get_last_name(self):
        return self.name.split(" ")[-1]
    
    def get_element(self):
        return self.element
    
    def get_rarity(self):
        return self.rarity
    
    def get_path(self):
        return self.path
    
    def get_image_path(self):
        # Thanks to u/jojocheck for compiling all the icons!
        parsed_name = self.name.replace(" ", "_")
        return os.path.join(dirname, f"../../assets/hsr_character_icons/{parsed_name}_Icon.png")
    
    def get_description(self):
        return f"{self.name} is a {self.rarity}⭐️ {self.element.name.capitalize()} {self.path.name.capitalize()} user in Honkai: Star Rail."

# Define all the characters
CHARACTERS = [

]


# Helper functions
def gen_character_dict(
        character: Character, 
        roles: list[str],
        light_cones: list[str],
        relics: list[str],
        main_stats: list[str],
        sub_stats: list[str],
        traces: list[str],
        tips: list[str], # for now still ability priority, might get changed later
        notes: str,
    ) -> dict[str, any]:
    return {
        "name": character.name,
        "element": character.element.name,
        "rarity": character.rarity,
        "path": character.path.name,
        "roles": roles,
        "light_cones": light_cones,
        "relics": relics,
        "main_stats": main_stats,
        "sub_stats": sub_stats,
        "traces": traces,
        "tips": tips,
        "notes": notes,
    }


def get_element_url(element: Element):
        return f"https://docs.google.com/spreadsheets/d/{SHEETS_KEY}/edit#gid={element.get_sheet_id()}"


async def save_dict_to_json(dictionary: dict[str, any]):
    file_name = dictionary["name"].lower().replace(" ", "_")
    try:
        with open(os.path.join(dirname, f"cache/{file_name}.json"), "w", encoding="utf-8") as f:
            json.dump(dictionary, f, indent=4)
    except Exception as e:
        print(f"Error saving {file_name} to json: {e}")


async def load_json_to_dict(character: Character) -> dict[str, any]:
    file_name = character.name.lower().replace(" ", "_")
    # check if file exists
    if not os.path.isfile(os.path.join(dirname, f"cache/{file_name}.json")):
        return None
    with open(os.path.join(dirname, f"cache/{file_name}.json"), "r", encoding="utf-8") as f:
        return json.load(f)
