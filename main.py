import discord
from discord.ext import commands
import asyncio
from time import sleep
from textwrap import dedent
from random import randrange
from modules.bot_gi_helper.bot_gi_helper import get_character_build
from utils.links import (
    EMBEDS_MAP_LINKS,
    EMBEDS_WIKI_LINKS,
    EMBEDS_BUILD_LINKS,
    EMBEDS_DB_LINKS,
)
 
# Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print('------------------')
    print('Logged in as')
    print(bot.user)
    print('------------------')


# ADMIN COMMANDS
@bot.command(name='sudo')
@commands.is_owner()
async def _sudo(ctx, *args):
    await ctx.send(f"### ACCESS GRANTED: {ctx.author} ###")
    if len(args) == 0:
        await ctx.send('*Please specify the command!*')
        return

    if args[0] == 'shutdown':
        await ctx.send('*Shutting down...*')
        await bot.close()
        return

@_sudo.error
async def sudo_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send(f'*WARNING: ACCESS DENIED!*\n{ctx.author} is not the admin!\nFurther trigger of this command will be reported to the admin!')
        return
    

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
        return

    if args[0] == 'map':
        await ctx.send(
            "### Genshin Impact Interactive Maps: 📍 ###",
            embeds=EMBEDS_MAP_LINKS
        )
    elif args[0] == 'wiki':
        await ctx.send(
            "### Genshin Impact Official Wiki: 🧐 ###",
            embeds=EMBEDS_WIKI_LINKS
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
                embeds=EMBEDS_BUILD_LINKS
            )
            return
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
                buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
                current = 0
                msg = await ctx.send(embed=results[0][current], file=discord.File(fp=results[1], filename="image.png"))

                for button in buttons:
                    await msg.add_reaction(button)

                while True:
                    try:
                        reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=90.0)

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
            embeds=EMBEDS_DB_LINKS
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



# @client.event
async def on_message(message):
    # GENERAL COMMANDS
    if message.content == '.hoo':
        channel = message.channel
        await channel.send('Hoo~')
    
    elif message.content == '.curse!':
        await message.channel.send('Noob!')

    elif message.content.startswith('.curse'):
        cursewords = ["Noob"] #, "Boo", "Asu", "Jancuk", "Fuck u", "Puki", "Cuki", "Jambret", "Jangkrik", "Anjing"]
        channel = message.channel
        if not message.mentions:
            await channel.send(f'{cursewords[randrange(len(cursewords))]}!')
            return
        
        for member in message.mentions:
            await channel.send(f'{cursewords[randrange(len(cursewords))]}! <@{member.id}> 👎')


    
    # HONKAI: STAR RAIL COMMANDS - TODO
    elif message.content.startswith('.hsr'):
        channel = message.channel
        hsr_content = message.content.split(' ')
        if len(hsr_content) == 1:
            await channel.send('Honkai Star Rail!')
        else:
            if hsr_content[1] == 'map':
                hsr_map = '[HoYoLAB](https://act.hoyolab.com/sr/app/interactive-map/index.html?lang=en-us#/map/)'
                await channel.send(f'!{hsr_map}')
 

# Run the client on the server
bot.run('MTEwMjk3OTQ2MzA0MzYxMjcxMw.GJtoDg.QDwZlZAr-N5VujaDhnDsITfXzPjcPffKEmPbfQ')