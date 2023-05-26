import discord
import os
from textwrap import dedent
from enum import Enum

# DEFINES - OTHERS
DIRNAME = os.path.dirname(__file__)
ERROR_IMAGE_PATH = os.path.join(DIRNAME, f"assets/shared/hotr_cried.jpg")
ERROR_IMAGE = discord.File(ERROR_IMAGE_PATH, filename="image.jpg")


class Modules(Enum):
    UNKNOWN, GI, HSR = range(3)

# ERRORS - SHARED
def error_character_not_found(module: Modules = Modules.DEFAULT, char_name: str = "X"):
    return dedent(f"""```ansi
    \u001b[0;31m{module.name} ERROR: Character Data for \u001b[4m{char_name}\u001b[0;31m not found!```"""
    )
