import discord
import os
from textwrap import dedent
from enum import Enum

# DEFINES - OTHERS
DIRNAME = os.path.dirname(__file__)
ERROR_IMAGE_PATH = os.path.join(DIRNAME, f"../assets/shared/hotr_cried.jpg")
ERROR_IMAGE_PATH_2 = os.path.join(DIRNAME, f"../assets/shared/bronya_angry.jpg")
ERROR_IMAGE_PATH_3 = os.path.join(DIRNAME, f"../assets/shared/bronya_confused.jpg")

class Modules(Enum):
    UNKNOWN, GI, HSR, HELP, SUDO = range(5)

def get_error_image(type: int = 0):
    if type == 0:
        return discord.File(ERROR_IMAGE_PATH, filename="hotr_cried.jpg")
    elif type == 1:
        return discord.File(ERROR_IMAGE_PATH_2, filename="bronya_angry.jpg")
    elif type == 2:
        return discord.File(ERROR_IMAGE_PATH_2, filename="bronya_confused.jpg")
    else:
        return discord.File(ERROR_IMAGE_PATH_2, filename="bronya_confused.jpg")

# ERRORS - SHARED
# CHARACTER NOT FOUND
def error_character_not_found(module: Modules = Modules.UNKNOWN, char_name: str = "unknown"):
    return dedent(f"""```ansi
\u001b[0;31m{module.name} ERROR: Character Data for \u001b[4m{char_name}\u001b[0;31m not found!```""")

# INVALID ARGUMENT
def error_invalid_option(module: Modules = Modules.UNKNOWN, arg: str = "unknown"):
    return dedent(f"""```ansi
\u001b[0;31m{module.name} ERROR: Invalid option \u001b[4m{arg}\u001b[0;31m!```""")
                  
# WRONG USAGE
def error_wrong_usage(module: Modules = Modules.UNKNOWN, cmd: str = "unknown"):
    return dedent(f"""```ansi
\u001b[0;31m{module.name} ERROR: Wrong usage! See .{str(module.name).lower()} {cmd} for more info!```""")
                  
# CATCHED ERROR
def error_catched(module: Modules = Modules.UNKNOWN, error = "unknown"):
    return dedent(f"""```ansi
\u001b[0;31m{module.name} ERROR: {error}```""")
                  

# ERRORS - SUDO
def error_access_denied(module: Modules = Modules.UNKNOWN, user: str = "unknown"):
    return dedent(f"""```ansi
\u001b[0;31mSUDO ERROR: ACCESS DENIED! 
User: \u001b[4m{user}\u001b[0;31m is not the admin!
Further trigger of this command will be reported to the admin!```""")

