import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio, sys, os
from textwrap import dedent
from random import randrange
from modules.bot_gi_helper.bot_gi_helper import (
    get_character_build as get_gi_character_build,
    get_all_characters_str as get_gi_all_characters_str
)
from modules.bot_hsr_helper.bot_hsr_helper import (
    get_character_build as get_hsr_character_build,
    get_all_characters_str as get_hsr_all_characters_str
)
from utils.embeds import (
    EMBEDS_GI_MAP_LINKS, EMBEDS_GI_WIKI_LINKS,
    EMBEDS_GI_BUILD_LINKS, EMBEDS_GI_DB_LINKS,
    EMBEDS_HSR_MAP_LINKS, EMBEDS_HSR_BUILD_LINKS,
    EMBEDS_HSR_DB_LINKS, EMBEDS_HSR_WIKI_LINKS
)
from utils.errors import (
    error_character_not_found, error_invalid_option,
    error_wrong_usage, error_access_denied,
    error_catched, get_bronya_image, Modules
)


# DEFINES
PREFIX = '.'
REBOOT = False
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)


# STARTUP
@bot.event
async def on_ready():
    print('------------------')
    print('Logged in as')
    print(bot.user)
    print('------------------')
    await bot.change_presence(activity=discord.Game(name='Project Bunny 19C, run .help for more info!'))
    # notify the admin that the bot is ready
    print(bot.application.owner)
    user = await bot.fetch_user(bot.application.owner.id)
    message, image = get_random_bronya_message()
    await user.send(f'### Bot on Standby! ###\n*{message}*', file=get_bronya_image(image))


# GENERAL HELP PAGE
HELP_MESSAGE = dedent(f"""\
## Welcome to Everything HoyoVerse Related Games! ##
Use `.gi [help]` to access Genshin Impact related commands!
Use `.hsr [help]` to access Honkai Star Rail related commands!
Use `.help` to access this page!

Other commands: TBD
""")
                      
@bot.command(name='help')
async def _help(ctx, *args):
    if len(args) == 0:
        await ctx.send(HELP_MESSAGE)
    else:
        await ctx.send(error_wrong_usage(Modules.UNKNOWN, 'help'), file=get_bronya_image(3))

@_help.error
async def help_error(ctx, error):
    await ctx.send(error_catched(Modules.HELP, error))


# GENSHIN IMPACT COMMANDS
GI_COMMANDS = [
    '.gi map - Interactive Map 📍\n', 
    '.gi wiki - Genshin Wikia 🧐\n', 
    '.gi db - Genshin Database, Wish Tracker 📚\n'
    '.gi chars - List of All Available Characters 📜\n'
    '.gi build - Characters Builds, Guides, and Theorycrafting 🤓\n', 
    '.gi build <character name> for character specific build ⭐️ (new!)',
]

GI_HELP_MESSAGE = dedent(f"""\
## Welcome to Everything Genshin Impact! ##
Usage: `.gi <commands>`
See available commands for more informations:
`{''.join(GI_COMMANDS)}`"""
)

@bot.command(name='gi')
async def _gi(ctx, *args):
    if len(args) == 0:
        await ctx.send(GI_HELP_MESSAGE)
    # GI MAP
    elif args[0] == 'map':
        await ctx.send(
            "## Genshin Impact Interactive Maps: 📍 ##",
            embeds=EMBEDS_GI_MAP_LINKS
        )
    # GI WIKI
    elif args[0] == 'wiki':
        await ctx.send(
            "## Genshin Impact Official Wiki: 🧐 ##",
            embeds=EMBEDS_GI_WIKI_LINKS
        )
    # GI CHARS
    elif args[0] == 'chars':
        if len(args) == 1:
            await ctx.send(
                dedent("""\
                    ## List of All Characters in Genshin Impact ##
                    Hint: Use `.gi chars <rarity>` to filter by rarity (5 Stars or 4 Stars)""")
            )
            for block in get_gi_all_characters_str(): await ctx.send(block)
        elif len(args) >= 2:
            rarity = args[1]
            if rarity in ('5', '4'):
                await ctx.send("## List of All Characters in Genshin Impact ##")
                for block in get_gi_all_characters_str(rarity=int(rarity)): await ctx.send(block)
            else:
                await ctx.send(error_invalid_option(Modules.GI, 'chars', rarity), file=get_bronya_image(3))
        else: 
            await ctx.send(error_wrong_usage(Modules.GI, "chars"), file=get_bronya_image(3))

    # GI BUILD
    elif args[0] == 'build':
        if len(args) == 1:
            await ctx.send(
                dedent("""\
                    ## Genshin Impact Characters Builds, Guides, and Theorycrafting: 🤓 ##
                    Use `.gi build <character name> [--full | --update]` for specific character build! ⭐️  (BETA)
                    Use `.gi chars` to get a list of all available characters.
                    Use the `--full` option to get the complete guide in one message. 
                    Use the `--update` option to discard cached data and get the latest build!
                    Use the **reaction buttons** to navigate through the pages. Please don't spam them! ⚠️"""),
                embeds=EMBEDS_GI_BUILD_LINKS
            )
        elif len(args) >= 2:
            build_flags = {'--full': False, '--update': False}
            char_name = []
            for arg in args[1:]:
                # replace em-dash with double dash
                arg = arg.replace('—', '--')
                if arg.startswith('--'):
                    if arg in build_flags:
                        build_flags[arg] = True
                    else:
                        await ctx.send(error_invalid_option(Modules.GI, arg), file=get_bronya_image(3))
                        return
                else:
                    char_name.append(arg)
            char_name = ' '.join(char_name)
            if char_name:
                results = await get_gi_character_build(char_name, not build_flags["--update"])
                if not results:
                    await ctx.send(error_character_not_found(Modules.GI, char_name), file=get_bronya_image(randrange(2)))
                    return
                # variables
                embeds = results[0]
                image_path = results[1]
                image_name = f'{char_name.replace(" ", "_").lower()}.png'
                # Force full page in DM
                if ctx.guild is None:
                    build_flags["--full"] = True
                    await ctx.send("DM only mode, forcing full page!")
                if build_flags["--full"]:
                    for c_e in embeds: 
                        await ctx.send(embed=c_e, file=discord.File(fp=image_path, filename=image_name))
                    return
                else:
                    await ctx.send(
                        dedent("""\
                        *Press the **reaction buttons** below to navigate through the pages.*
                        *Use the `--full` option to get the complete guide in one long message.*""")
                )
                # MULTI PAGE EMBEDS
                buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
                current = 0
                msg = await ctx.send(embed=embeds[current], file=discord.File(fp=image_path, filename=image_name))
                for button in buttons: await msg.add_reaction(button)
                while True:
                    try:
                        reaction, user = await bot.wait_for(
                            "reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=90.0
                        )
                    except asyncio.TimeoutError as e:
                        embed = embeds[current]
                        embed.set_footer(text="Timed out!")
                        await msg.clear_reactions()
                    else:
                        previous_page = current
                        if reaction.emoji == u"\u23EA":
                            current = 0
                        elif reaction.emoji == u"\u25C0":
                            if current > 0:
                                current -= 1
                        elif reaction.emoji == u"\u25B6":
                            if current < len(embeds) - 1:
                                current += 1
                        elif reaction.emoji == u"\u23E9":
                            current = len(embeds) - 1

                        for button in buttons: await msg.remove_reaction(button, ctx.author)
                        if current != previous_page:
                            await msg.edit(embed=embeds[current])
            else:
                await ctx.send(error_wrong_usage(Modules.GI, "build"), file=get_bronya_image(3))
    elif args[0] == 'db':
        await ctx.send(
            "## Genshin Impact Database: 📚 ##",
            embeds=EMBEDS_GI_DB_LINKS
        )
    elif args[0] == 'help':
        await ctx.send(GI_HELP_MESSAGE)
    else:
        await ctx.send(error_wrong_usage(Modules.GI, "help"), file=get_bronya_image(3))

@_gi.error
async def gi_error(ctx, error):
    await ctx.send(error_catched(Modules.GI, error), file=get_bronya_image(3))


# HONKAI: STAR RAIL COMMANDS
HSR_COMMANDS = [
    '.hsr map - Interactive Map(s) 📍\n', 
    '.hsr wiki - Honkai: Star Rail Wiki 🧐\n', 
    '.hsr db - Honkai: Star Rail Database, Warp Tracker, Tierlist 📚\n'
    '.hsr chars - List of All Available Characters 📜\n'
    '.hsr build - Characters Builds, Guides, and Theorycrafting 🤓\n', 
    '.hsr build <character name> - Specific Character Build ⭐️ (new!)'
]

HSR_HELP_MESSAGE = dedent(f"""\
## Welcome to Everything Honkai: Star Rail! ##
Usage: `.hsr <commands>`
See available commands for more informations:
`{''.join(HSR_COMMANDS)}`"""
)
                          
@bot.command(name='hsr')
async def _hsr(ctx, *args):
    if len(args) == 0:
        await ctx.send(HSR_HELP_MESSAGE)
    # HSR MAP
    elif args[0] == 'map':
        await ctx.send(
            "## Honkai Star Rail Interactive Maps: 📍 ##",
            embeds=EMBEDS_HSR_MAP_LINKS
        )
    # HSR WIKI
    elif args[0] == 'wiki':
        await ctx.send(
            "## Honkai Star Rail Official Wiki: 🧐 ##",
            embeds=EMBEDS_HSR_WIKI_LINKS
        )
    # HSR CHARS
    elif args[0] == 'chars':
        if len(args) == 1:
            await ctx.send(
                dedent("""\
                    ## List of All Characters in Honkai: Star Rail ##
                    Hint: Use `.hsr chars <rarity>` to filter by rarity (5 Stars or 4 Stars)""")
            )
            for block in get_hsr_all_characters_str(): await ctx.send(block)
        elif len(args) >= 2:
            rarity = args[1]
            if rarity in ('5', '4'):
                await ctx.send("## List of All Characters in Honkai: Star Rail ##")
                for block in get_hsr_all_characters_str(rarity=int(rarity)): await ctx.send(block)
            else:
                await ctx.send(error_invalid_option(Modules.HSR, 'chars', rarity), file=get_bronya_image(3))
        else: 
            await ctx.send(error_wrong_usage(Modules.HSR, "chars"), file=get_bronya_image(3))
    # HSR BUILD
    elif args[0] == 'build':
        if len(args) == 1:
            await ctx.send(
                dedent("""\
                    ## Honkai: Star Rail Characters Builds, Guides, and Theorycrafting: 🤓 ##
                    Use `.hsr build <character name> [--full | --update]` for specific character build! ⭐️  (BETA)
                    Use `.hsr chars` to get a list of all available characters.
                    Use the `--full` option to get the complete guide in one long message. 
                    Use the `--update` option to discard cached data and get the latest build!
                    Use the **reaction buttons** to navigate through the pages. Please don't spam them! ⚠️"""),
                embeds=EMBEDS_HSR_BUILD_LINKS
            )
        elif len(args) >= 2:
            build_flags = {'--full': False, '--update': False}
            char_name = []
            for arg in args[1:]:
                # replace em-dash with double dash
                arg = arg.replace('—', '--')
                if arg.startswith('--'):
                    if arg in build_flags:
                        build_flags[arg] = True
                    else:
                        await ctx.send(error_invalid_option(Modules.HSR, arg), file=get_bronya_image(3))
                        return
                else:
                    char_name.append(arg)
            char_name = ' '.join(char_name)
            if char_name:
                results = await get_hsr_character_build(char_name, not build_flags["--update"])
                if not results:
                    await ctx.send(error_character_not_found(Modules.HSR, char_name), file=get_bronya_image(randrange(2)))
                    return
                # variables
                embeds = results[0]
                icon_file = results[1]
                # Force full page in DM
                if ctx.guild is None:
                    build_flags["--full"] = True
                    await ctx.send("DM only mode, forcing full page!")
                if build_flags["--full"]:
                    for embed in embeds: 
                        await ctx.send(embed=embed, file=discord.File(*icon_file))
                    return
                else:
                    await ctx.send(
                        dedent("""\
                        *Press the **reaction buttons** below to navigate through the pages.*
                        *Use the `--full` option to get the complete guide in one long message.*""")
                )
                # MULTI PAGE EMBEDS
                buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
                current = 0
                msg = await ctx.send(embed=embeds[current], file=discord.File(*icon_file))
                for button in buttons: await msg.add_reaction(button)
                while True:
                    try:
                        reaction, user = await bot.wait_for(
                            "reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=90.0
                        )
                    except asyncio.TimeoutError as e:
                        embed = embeds[current]
                        embed.set_footer(text="Timed out!")
                        await msg.clear_reactions()
                    else:
                        previous_page = current
                        if reaction.emoji == u"\u23EA":
                            current = 0
                        elif reaction.emoji == u"\u25C0":
                            if current > 0:
                                current -= 1
                        elif reaction.emoji == u"\u25B6":
                            if current < len(embeds) - 1:
                                current += 1
                        elif reaction.emoji == u"\u23E9":
                            current = len(embeds) - 1

                        for button in buttons: await msg.remove_reaction(button, ctx.author)
                        if current != previous_page:
                            await msg.edit(embed=embeds[current])
            else:
                await ctx.send(error_wrong_usage(Modules.HSR, "build"), file=get_bronya_image(3))
    # HSR DB
    elif args[0] == 'db':
        await ctx.send(
            "## Honkai Star Rail Database: 📚 ##",
            embeds=EMBEDS_HSR_DB_LINKS
        )
    elif args[0] == 'help':
        await ctx.send(HSR_HELP_MESSAGE)
    else:
        await ctx.send(error_wrong_usage(Modules.HSR, "help"), file=get_bronya_image(3))

@_hsr.error
async def hsr_error(ctx, error):
    await ctx.send(error_catched(Modules.HSR, error), file=get_bronya_image(3))


# OTHER COMMANDS
@bot.command(name='hoo')
async def _hoo(ctx):
    await ctx.send('Hoo~ 🫢')

@bot.command(name='curse')
async def _curse(ctx, *args):
    cursewords_base = ["Noob", "Boo", "Lame", "Skill issue", "Asu", "Jancuk", "Fuck u", "Puki", "Cuki", "Jambret", "Jangkrik", "Anjing"]
    cursewords = cursewords_base if len(args) > 0 and '!' in args else cursewords_base[:4]
    # check if there is ! after command    
    if len(args) == 0 or len(args) == 1 and args[0] == '!':
        await ctx.send(f'{cursewords[randrange(len(cursewords))]}!')
        return
    
    for member in ctx.message.mentions:
        await ctx.send(f'{cursewords[randrange(len(cursewords))]}! <@{member.id}> 👎')

# TO BE DELETED!
@bot.command(name='ajkk')
async def _ajkk(ctx, *args):
    if len(args) == 0:
        await ctx.send("Wana!")
        return
    for member in ctx.message.mentions:
        await ctx.send(f'Wana kon! <@{member.id}>')

# funzies, real dialogue by Bronya battlesuits in HI3
bronya_messages = [
    ("Project bunny, immediately startup the Captain cleansing program. 😑", 2),
    ("Bronya is observing where Captain's IQ flew off to. 🤔", 1),
    ("Captain, do you want to test what gravity feels like? 😏", 2),
    ("Detected an emotion fluctuating, is Bronya broken? 😳", 3),
    ("This is Bronya's first time realizing bridge duty is boring. 🫠", 3),
    ("Project Bunny 19C, now is not the time to be dozing off. 😤", 1),
    ("Bronya, on standby. 🫡", 5),
    ("Bronya, mood declining. 😒", 3),
    ("Captain, Project Bunny also wants to play games with you. 😊", 5),
    ("Put up both hands and place them behind your head. Captain, you are being arrested. 😠", 2),
    ("If there\'s no work, can Bronya go home to play games? 🥹", 4),
    ("Time together with Captain, Bronya is very happy. 😊", 4),
    ("Good evening Captain... I mean morning. 😄", 1),
    ("Since we have the day off... Wanna join Bronya for some game, Captain? 😅", 4),
    ("Just order whatever you want and let Project Bunny do the cookin. 😌", 5),
    ("Today's work turned out perfect. And the rest... we'll save for Project Bunny 😌", 5),
    ("Next time, maybe Seele can ride on Project Bunny and we can go touring together. 😊", 5),
    ("As long as Bronya keep moving forward... this legacy will continue to grow. 🫡", 4),
    ("I was thinking about something... were you too Captain? 😕", 1),
    ("The analysis shows that Captain really needs some rest. 😴", 4),
    
]

def get_random_bronya_message():
    rand = randrange(len(bronya_messages))
    return bronya_messages[rand]

@bot.command(name='bronya')
async def _bronya(ctx, *args):
    message, image = get_random_bronya_message()
    if len(args) == 0:
        await ctx.send(f"*{message}*", file=get_bronya_image(image))


# ADMIN COMMANDS
@bot.command(name='sudo')
@commands.is_owner()
async def _sudo(ctx, *args):
    await ctx.send(f"### ACCESS GRANTED: {ctx.author} ###")
    if len(args) == 0:
        await ctx.send('*Please specify the command!*')

    elif args[0] == 'shutdown':
        await ctx.send('*Shutting down...*\n\u200e')
        await bot.close()
    
    elif args[0] == 'reboot':
        global REBOOT
        await ctx.send('*Rebooting...*\n\u200e')
        REBOOT = True
        await bot.close()

    elif args[0] == 'remote-status':
        await ctx.send('*Checking remote status...*')
        res = os.system("git remote update")
        if res == 0:
            await ctx.send('*Remote status check successful!*\n\u200e')
        else:
            await ctx.send(error_catched(Modules.SUDO, "Remote status check failed!"))
            return
        if os.popen("git rev-parse HEAD").read() == os.popen("git rev-parse @{u}").read():
            await ctx.send('*Bot is up to date!*\n\u200e')
        else:
            await ctx.send('*There are changes to pull, please update!*\n\u200e')
    
    elif args[0] == 'update':
        await ctx.send('*Updating...*')
        res = os.system("git pull")
        if res == 0:
            await ctx.send('*Update successful!*')
        else:
            await ctx.send(error_catched(Modules.SUDO, "Update failed!"))
            return
        # check if the main.py still can be compiled
        res = os.system(f"python3 -m py_compile {sys.argv[0]}")
        if res == 0:
            REBOOT = True
            await ctx.send('*Rebooting...*\n\u200e')
            await bot.close()
        else:
            await ctx.send(error_catched(Modules.SUDO, "Update failed! Cannot compile the program."))

    elif args[0] == 'clear-cache':
        if len(args) == 1:
            await ctx.send('*Please specify the cache to clear!*')
            return
        else:
            res = 0
            if args[1] == 'hsr':
                await ctx.send('*Clearing HSR cache...*')
                res = os.system("rm -rf modules/bot_hsr_helper/cache/*")
            elif args[1] == 'gi':
                await ctx.send('*Clearing GI cache...*')
                res = os.system("rm -rf modules/bot_gi_helper/cache/*")
            elif args[1] == 'all':
                await ctx.send('*Clearing all cache...*')
                res1 = os.system("rm -rf modules/bot_hsr_helper/cache/*")
                res2 = os.system("rm -rf modules/bot_gi_helper/cache/*")
                res = res1 + res2
            if res == 0:
                await ctx.send('*Clearing successful!*\n\u200e')
            else:
                await ctx.send(f"{error_catched(Modules.SUDO, 'Clearing failed!')}\n\u200e")
    
    elif args[0] == "test":
        await ctx.send("Test")

    else:
        await ctx.send(error_catched(Modules.SUDO, f"Invalid command! {args[0]}"))

@_sudo.error
async def sudo_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send(error_access_denied(Modules.SUDO, ctx.author), file=get_bronya_image(2))
    else:
        await ctx.send(error_catched(Modules.SUDO, error))


# Run the client on the server
load_dotenv()
BOT_API_KEY = os.getenv('BOT_API_KEY')
bot.run(BOT_API_KEY)

if REBOOT:
    print("Rebooting now...")
    os.execv(sys.executable, ['python3'] + sys.argv)
