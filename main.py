import discord
from discord.ext import commands
import asyncio
import sys, os
from textwrap import dedent
from random import randrange
from modules.bot_gi_helper.bot_gi_helper import get_character_build
from utils.links import (
    EMBEDS_GI_MAP_LINKS, EMBEDS_GI_WIKI_LINKS,
    EMBEDS_GI_BUILD_LINKS, EMBEDS_GI_DB_LINKS,
    EMBEDS_HSR_MAP_LINKS,
)


# DEFINES
INTENTS = discord.Intents.default()
INTENTS.message_content = True
RESTART = False
bot = commands.Bot(command_prefix='.', intents=INTENTS)


# STARTUP
@bot.event
async def on_ready():
    print('------------------')
    print('Logged in as')
    print(bot.user)
    print('------------------')
    await bot.change_presence(activity=discord.Game(name='Project Bunny 19C, run .hoyo for more info!'))
    # notify the admin that the bot is ready
    print(bot.application.owner)
    user = await bot.fetch_user(bot.application.owner.id)
    await user.send('**Bot on Standby!**\n*Bronya is observing where Captain\'s IQ flew off to. 🤔*')


# GENERAL HELP PAGE
HELP_MESSAGE = dedent(f"""\
## Welcome to Everything HoyoVerse Related Games! ##
Use `.gi [help]` to access Genshin Impact related commands!
Use `.hsr [help]` to access Honkai Star Rail related commands!
Use `.hoyo` to access this page!

Other commands: TBD
""")
                      
@bot.command(name='hoyo')
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
    '.gi db - Genshin Database 📚'
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
                    Use `.gi build <character name> [--full | --no-cache]` for specific character build! ⭐️  (BETA)
                    Use the `--full` option to get the complete guide in one message (Works on DM). 
                    Use the `--no-cache` option to discard cached data and get the latest build!
                    Please don't spam the reaction buttons! ⚠️"""),
                embeds=EMBEDS_GI_BUILD_LINKS
            )
        elif len(args) >= 2:
            char_name = ' '.join([arg for arg in args[1:] if not arg.startswith('-')])
            if char_name:
                results = get_character_build(char_name, False if '--no-cache' in args[1:] else True)
                if not results:
                    await ctx.send(f"Error: Character Data for *{char_name}* not found!")
                    return
                if "--full" in args[1:]:
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
                    except asyncio.TimeoutError:
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

                        for button in buttons:
                            await msg.remove_reaction(button, ctx.author)

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
    # '.hsr wiki - Honkai Star Rail Wiki 🧐\n', 
    # '.hsr build - Character Builds and Guides 🤓\n', 
    # '.hsr db - Honkai Star Rail Database 📚'
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
    elif args[0] == 'map':
        await ctx.send(
            "### Honkai Star Rail Interactive Maps: 📍 ###",
            embeds=EMBEDS_HSR_MAP_LINKS
        )
    # elif args[0] == 'wiki':
    #     await ctx.send(
    #         "### Honkai Star Rail Official Wiki: 🧐 ###",
    #         embeds=EMBEDS_GI_WIKI_LINKS
    #     )
    # elif args[0] == 'build':
    #     await ctx.send(
    #         "### Honkai Star Rail Character Builds and Guides: 🤓 ###",
    #         embeds=EMBEDS_GI_BUILD_LINKS
    #     )
    # elif args[0] == 'db':
    #     await ctx.send(
    #         "### Honkai Star Rail Database: 📚 ###",
    #         embeds=EMBEDS_GI_DB_LINKS
    #     )
    elif args[0] == 'help':
        await ctx.send(HSR_HELP_MESSAGE)
    else:
        await ctx.send("Wrong command! See `.hsr help` for more info.")

@_hsr.error
async def hsr_error(ctx, error):
    await ctx.send(f"ERROR_HSR: {error}")


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
                       "Bronya is observing where Captain's IQ flew off to. 🤔"]
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
    
    elif args[0] == 'restart':
        global RESTART
        await ctx.send('*Restarting...*\n\u200e')
        RESTART = True
        await bot.close()
    
    elif args[0] == 'update':
        await ctx.send('*Updating...*\n')
        os.system("git pull")
        RESTART = True
        await ctx.send('*Restarting...*\n\u200e')
        await bot.close()
    
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

if RESTART:
    print("Restarting now")
    os.execv(sys.executable, ['python3'] + sys.argv)
