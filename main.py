import discord
from discord.ext import commands
import asyncio, sys, os
from textwrap import dedent
from random import randrange
from modules.bot_gi_helper.bot_gi_helper import (
    get_character_build as get_gi_character_build
)
from modules.bot_hsr_helper.bot_hsr_helper import (
    get_character_build as get_hsr_character_build
)
from utils.links import (
    EMBEDS_GI_MAP_LINKS, EMBEDS_GI_WIKI_LINKS,
    EMBEDS_GI_BUILD_LINKS, EMBEDS_GI_DB_LINKS,
    EMBEDS_HSR_MAP_LINKS, EMBEDS_HSR_BUILD_LINKS,
    EMBEDS_HSR_DB_LINKS, EMBEDS_HSR_WIKI_LINKS
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
    await user.send('**Bot on Standby!**\n*Time together with Captain, Bronya is very happy. 😊*')


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
        await ctx.send("Wrong command! See `.help` for more info.")

@_help.error
async def help_error(ctx, error):
    await ctx.send(f"ERROR_HELP: {error}")


# GENSHIN IMPACT COMMANDS
GI_COMMANDS = [
    '.gi map - Interactive Map 📍\n', 
    '.gi wiki - Genshin Wikia 🧐\n', 
    '.gi build - Character Builds and Guides 🤓\n', 
    '.gi db - Genshin Database, Wish Tracker 📚'
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

    elif args[0] == 'map':
        await ctx.send(
            "### Genshin Impact Interactive Maps: 📍 ###",
            embeds=EMBEDS_GI_MAP_LINKS
        )
    elif args[0] == 'wiki':
        await ctx.send(
            "### Genshin Impact Official Wiki: 🧐 ###",
            embeds=EMBEDS_GI_WIKI_LINKS
        )
    elif args[0] == 'build':
        if len(args) == 1:
            await ctx.send(
                dedent("""\
                    ### Genshin Impact Character Builds and Guides: 🤓 ###
                    Use `.gi build <character name> [--full | --update]` for specific character build! ⭐️  (BETA)
                    Use the `--full` option to get the complete guide in one message. 
                    Use the `--update` option to discard cached data and get the latest build!
                    Please don't spam the reaction buttons! ⚠️"""),
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
                        await ctx.send(f"Error: Invalid option *{arg}*!")
                        return
                else:
                    char_name.append(arg)
            char_name = ' '.join(char_name)
            print("CHAR NAME:", char_name)
            if char_name:
                results = await get_gi_character_build(char_name, not build_flags["--update"])
                if not results:
                    await ctx.send(f"Error: Character Data for *{char_name}* not found!")
                    return
                # Force full page in DM
                if ctx.guild is None:
                    build_flags["--full"] = True
                    await ctx.send("DM only mode, forcing full page!")
                if build_flags["--full"]:
                    [await ctx.send(embed=c_e, file=discord.File(fp=results[1], filename="image.png")) for c_e in results[0]]
                    return
                
                # MULTI PAGE EMBEDS
                buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
                current = 0
                msg = await ctx.send(embed=results[0][current], file=discord.File(fp=results[1], filename="image.png"))
                [await msg.add_reaction(button) for button in buttons]
                    
                while True:
                    try:
                        reaction, user = await bot.wait_for(
                            "reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=90.0
                        )
                    except asyncio.TimeoutError as e:
                        embed = results[0][current]
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
                            if current < len(results[0]) - 1:
                                current += 1
                        elif reaction.emoji == u"\u23E9":
                            current = len(results[0]) - 1

                        [await msg.remove_reaction(button, ctx.author) for button in buttons]
                        if current != previous_page:
                            await msg.edit(embed=results[0][current])
            else:
                await ctx.send("Error: Wrong Usage! See .gi build for more info.")
    elif args[0] == 'db':
        await ctx.send(
            "### Genshin Impact Database: 📚 ###",
            embeds=EMBEDS_GI_DB_LINKS
        )
    elif args[0] == 'help':
        await ctx.send(GI_HELP_MESSAGE)
    else:
        await ctx.send("Wrong command! See `.gi help` for more info.")

@_gi.error
async def gi_error(ctx, error):
    await ctx.send(f"ERROR_GI: {error}")


# HONKAI: STAR RAIL COMMANDS
HSR_COMMANDS = [
    '.hsr map - Interactive Map 📍\n', 
    '.hsr wiki - Honkai Star Rail Wiki 🧐\n', 
    '.hsr build - Character Builds and Guides 🤓\n', 
    '.hsr db - Honkai Star Rail Database, Warp Tracker, Tierlist 📚'
]

HSR_HELP_MESSAGE = dedent(f"""\
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
            "### Honkai Star Rail Interactive Maps: 📍 ###",
            embeds=EMBEDS_HSR_MAP_LINKS
        )
    # HSR WIKI
    elif args[0] == 'wiki':
        await ctx.send(
            "### Honkai Star Rail Official Wiki: 🧐 ###",
            embeds=EMBEDS_HSR_WIKI_LINKS
        )
    # HRS BUILD
    elif args[0] == 'build':
        if len(args) == 1:
            await ctx.send(
                dedent("""\
                    ### Honkai: Star Rail Character Builds and Guides: 🤓 ###
                    Use `.hsr build <character name> [--full | --update]` for specific character build! ⭐️  (BETA)
                    Use the `--full` option to get the complete guide in one message. 
                    Use the `--update` option to discard cached data and get the latest build!
                    Please don't spam the reaction buttons! ⚠️"""),
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
                        await ctx.send(f"Error: Invalid option *{arg}*!")
                        return
                else:
                    char_name.append(arg)
            char_name = ' '.join(char_name)
            if char_name:
                results = await get_hsr_character_build(char_name, not build_flags["--update"])
                if not results:
                    await ctx.send(f"Error: Character Data for *{char_name}* not found!")
                    return
                
                # Force full page in DM
                if ctx.guild is None:
                    build_flags["--full"] = True
                    await ctx.send("DM only mode, forcing full page!")
                if build_flags["--full"]:
                    [await ctx.send(embed=c_e, file=discord.File(fp=results[1], filename="image.png")) for c_e in results[0]]
                    return
                
                # MULTI PAGE EMBEDS
                buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
                current = 0
                msg = await ctx.send(embed=results[0][current], file=discord.File(fp=results[1], filename="image.png"))
                [await msg.add_reaction(button) for button in buttons]
                    
                while True:
                    try:
                        reaction, user = await bot.wait_for(
                            "reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=90.0
                        )
                    except asyncio.TimeoutError as e:
                        embed = results[0][current]
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
                            if current < len(results[0]) - 1:
                                current += 1
                        elif reaction.emoji == u"\u23E9":
                            current = len(results[0]) - 1

                        [await msg.remove_reaction(button, ctx.author) for button in buttons]
                        if current != previous_page:
                            await msg.edit(embed=results[0][current])
            else:
                await ctx.send("Error: Wrong Usage! See .hsr build for more info.")
    # HSR DB
    elif args[0] == 'db':
        await ctx.send(
            "### Honkai Star Rail Database: 📚 ###",
            embeds=EMBEDS_HSR_DB_LINKS
        )
    elif args[0] == 'help':
        await ctx.send(HSR_HELP_MESSAGE)
    else:
        await ctx.send("Wrong command! See `.hsr help` for more info.")

# @_hsr.error
# async def hsr_error(ctx, error):
#     await ctx.send(f"ERROR_HSR: {error}")


# OTHER COMMANDS
@bot.command(name='hoo')
async def _hoo(ctx):
    await ctx.send('Hoo~ 🫢')

@bot.command(name='curse')
async def _curse(ctx, *args):
    cursewords_base = ["Noob", "Boo", "Lame", "Asu", "Jancuk", "Fuck u", "Puki", "Cuki", "Jambret", "Jangkrik", "Anjing"]
    cursewords = cursewords_base if len(args) > 0 and '!' in args else cursewords_base[:3]
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

@bot.command(name='bronya')
async def _bronya(ctx, *args):
    bronya_messages = ["Project bunny, immediately startup the Captain cleansing program. 😑", 
                       "Bronya is observing where Captain's IQ flew off to. 🤔",
                       "Captain, do you want to test what gravity feels like? 😏",
                       "Detected an emotion fluctuating, is Bronya broken? 😳",
                       "This is Bronya's first time realizing bridge duty is boring. 😴",
                       "Project Bunny 19C, now is not the time to be dozing off. 😤",
                       "Bronya, on standby. 🫡",
                       "Bronya, mood declining. 😒",
                       "Captain, Project Bunny also wants to play games with you. 😊",
                       "Put up both hands and place them behind your head. Captain, you are being arrested. 😠",
                       "If there’s no work, can Bronya go home to play games? 🫠"]
    if len(args) == 0:
        await ctx.send(f"*{bronya_messages[randrange(len(bronya_messages))]}*")
    


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
            await ctx.send('*Error: Remote status check failed!*\n\u200e')
            return
        
        res = os.system("git status -uno")
        if res == 0:
            await ctx.send('*No updates available!*\n\u200e')
        else:
            await ctx.send('*Updates available!*\n\u200e')
    
    elif args[0] == 'update':
        await ctx.send('*Updating...*')
        res = os.system("git pull")
        if res == 0:
            await ctx.send('*Update successful!*\n\u200e')
        else:
            await ctx.send('*Error: Update failed!*\n\u200e')
            return
        REBOOT = True
        await ctx.send('*Rebooting...*\n\u200e')
        await bot.close()

    elif args[0] == 'clear-cache':
        if len(args) == 1:
            await ctx.send('*Please specify the cache to clear!*')
            return
        if args[1] == 'hsr':
            await ctx.send('*Clearing HSR cache...*')
            res = os.system("rm -rf modules/bot_hsr_helper/cache/*")
            if res == 0:
                await ctx.send('*Clearing successful!*\n\u200e')
            else:
                await ctx.send('*Error: Clearing failed!*\n\u200e')
        elif args[1] == 'gi':
            await ctx.send('*Clearing GI cache...*')
            res = os.system("rm -rf modules/bot_gi_helper/cache/*")
            if res == 0:
                await ctx.send('*Clearing successful!*\n\u200e')
            else:
                await ctx.send('*Error: Clearing failed!*\n\u200e')
    
    elif args[0] == "test":
        await ctx.send("Test")

    else:
        await ctx.send(f"*Unknown command: {args[0]}*")

@_sudo.error
async def sudo_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send(f'*WARNING: ACCESS DENIED!*\n{ctx.author} is not the admin!\nFurther trigger of this command will be reported to the admin!')
    else:
        await ctx.send(f"ERROR_SUDO: {error}")


# Run the client on the server
bot.run('MTEwMjk3OTQ2MzA0MzYxMjcxMw.GJtoDg.QDwZlZAr-N5VujaDhnDsITfXzPjcPffKEmPbfQ')

if REBOOT:
    print("Rebooting now...")
    os.execv(sys.executable, ['python3'] + sys.argv)
