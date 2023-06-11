import discord
import os
from textwrap import dedent
from enum import Enum

# DEFINES - OTHERS
DIRNAME = os.path.dirname(__file__)

class Modules(Enum):
    UNKNOWN, GI, HSR, HELP, SUDO = range(5)

def get_bronya_image(type: int = 0):
    image_name_ext = ""
    if type == 0:
        image_name_ext = "hotr_cried.jpg"
    elif type == 1:
        image_name_ext = "bronya_confused.jpg"
    elif type == 2:
        image_name_ext = "bronya_angry.jpg"
    elif type == 3:
        image_name_ext = "bronya_not_responding.jpg"
    elif type == 4:
        image_name_ext = "bronya_welcome.jpg"
    elif type == 5:
        image_name_ext = "bronya_project_bunny.jpg"
    else:
        image_name_ext = "bronya_not_responding.jpg"
    return discord.File(
        os.path.join(DIRNAME, f"../assets/shared/{image_name_ext}"), 
        filename=f"{image_name_ext}"
    )

# ERRORS - SHARED
# CHARACTER NOT FOUND
def error_character_not_found(module: Modules = Modules.UNKNOWN, char_name: str = "unknown"):
    return dedent(f"""```ansi
\u001b[0;31m{module.name} ERROR: Character Data for \u001b[4m{char_name}\u001b[0;31m not found!
Use \".hsr | .gi chars\" to see the list of available characters!```""")

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

