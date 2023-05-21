from enum import Enum
import os
import json

# The key for the google sheets
# Source: [Genshin Impact Helper's Team](https://docs.google.com/spreadsheets/d/1gNxZ2xab1J6o1TuNVWMeLOZ7TPOqrsf3SshP5DLvKzI)
SHEETS_KEY = "1gNxZ2xab1J6o1TuNVWMeLOZ7TPOqrsf3SshP5DLvKzI"
SHEET_CHANGELOGS_ID = "172546500"
SHEET_PYRO_ID = "954718212"
SHEET_HYDRO_ID = "1354385732"
SHEET_ELECTRO_ID = "408609723"
SHEET_DENDRO_ID = "1468017260"
SHEET_CRYO_ID = "1169063456"
SHEET_ANEMO_ID = "653464458"
SHEET_GEO_ID = "1780570478"

dirname = os.path.dirname(__file__)

# Enum for the elements
class Element(Enum):
    PYRO = 1; HYDRO = 2; ELECTRO = 3;
    DENDRO = 4; CRYO = 5; ANEMO = 6; GEO = 7

    def get_sheet_id(self):
        if self == Element.PYRO:
            return SHEET_PYRO_ID
        elif self == Element.HYDRO:
            return SHEET_HYDRO_ID
        elif self == Element.ELECTRO:
            return SHEET_ELECTRO_ID
        elif self == Element.DENDRO:
            return SHEET_DENDRO_ID
        elif self == Element.CRYO:
            return SHEET_CRYO_ID
        elif self == Element.ANEMO:
            return SHEET_ANEMO_ID
        elif self == Element.GEO:
            return SHEET_GEO_ID
        else:
            return None
        
# Enum for the weapon types
class WeaponType(Enum):
    SWORD = 1; CLAYMORE = 2; POLEARM = 3; BOW = 4; CATALYST = 5

# Class for the characters
class Character():
    def __init__(self, name: str, element: Element, rarity: int, weapon_type: WeaponType):
        self.name = name
        self.element = element
        self.rarity = rarity
        self.weapon_type = weapon_type

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
    
    def get_weapon_type(self):
        return self.weapon_type
    
    def get_image_path(self):
        # Thanks to u/jojocheck for compiling all the icons!
        parsed_name = self.name.replace(" ", "_")
        return os.path.join(dirname, f"../../assets/character_icons/{parsed_name}_Icon.png")
    
    def get_description(self):
        return f"{self.name} is a {self.rarity}⭐️ {self.element.name.lower()} {self.weapon_type.name.lower()} user in Genshin Impact."

# Define all the characters
CHARACTERS = [
    Character("Albedo", Element.GEO, 5, WeaponType.SWORD),
    Character("Alhaitham", Element.DENDRO, 5, WeaponType.SWORD),
    Character("Aloy", Element.CRYO, 5, WeaponType.BOW),
    Character("Amber", Element.PYRO, 4, WeaponType.BOW),
    Character("Arataki Itto", Element.GEO, 5, WeaponType.CLAYMORE),
    Character("Baizhu", Element.DENDRO, 5, WeaponType.CATALYST),
    Character("Barbara", Element.HYDRO, 4, WeaponType.CATALYST),
    Character("Beidou", Element.ELECTRO, 4, WeaponType.CLAYMORE),
    Character("Bennett", Element.PYRO, 4, WeaponType.SWORD),
    Character("Candace", Element.HYDRO, 4, WeaponType.POLEARM),
    Character("Chongyun", Element.CRYO, 4, WeaponType.CLAYMORE),
    Character("Collei", Element.DENDRO, 4, WeaponType.BOW),
    Character("Cyno", Element.ELECTRO, 5, WeaponType.POLEARM),
    Character("Dehya", Element.PYRO, 5, WeaponType.CLAYMORE),
    Character("Diluc", Element.PYRO, 5, WeaponType.CLAYMORE),
    Character("Diona", Element.CRYO, 4, WeaponType.BOW),
    Character("Dori", Element.ELECTRO, 4, WeaponType.CLAYMORE),
    Character("Eula", Element.CRYO, 5, WeaponType.CLAYMORE),
    Character("Faruzan", Element.ANEMO, 4, WeaponType.BOW),
    Character("Fischl", Element.ELECTRO, 4, WeaponType.BOW),
    Character("Ganyu", Element.CRYO, 5, WeaponType.BOW),
    Character("Gorou", Element.GEO, 4, WeaponType.BOW),
    Character("Hu Tao", Element.PYRO, 5, WeaponType.POLEARM),
    Character("Jean", Element.ANEMO, 5, WeaponType.SWORD),
    Character("Kaedehara Kazuha", Element.ANEMO, 5, WeaponType.SWORD),
    Character("Kaeya", Element.CRYO, 4, WeaponType.SWORD),
    Character("Kamisato Ayaka", Element.CRYO, 5, WeaponType.SWORD),
    Character("Kamisato Ayato", Element.HYDRO, 5, WeaponType.SWORD),
    Character("Kaveh", Element.DENDRO, 4, WeaponType.CLAYMORE),
    Character("Keqing", Element.ELECTRO, 5, WeaponType.SWORD),
    Character("Klee", Element.PYRO, 5, WeaponType.CATALYST),
    Character("Kujou Sara", Element.ELECTRO, 4, WeaponType.BOW),
    Character("Kuki Shinobu", Element.ELECTRO, 4, WeaponType.SWORD),
    Character("Layla", Element.CRYO, 4, WeaponType.BOW),
    Character("Lisa", Element.ELECTRO, 4, WeaponType.CATALYST),
    Character("Mika", Element.CRYO, 4, WeaponType.POLEARM),
    Character("Mona", Element.HYDRO, 5, WeaponType.CATALYST),
    Character("Nahida", Element.DENDRO, 5, WeaponType.CATALYST),
    Character("Nilou", Element.HYDRO, 5, WeaponType.SWORD),
    Character("Ningguang", Element.GEO, 4, WeaponType.CATALYST),
    Character("Noelle", Element.GEO, 4, WeaponType.CLAYMORE),
    Character("Qiqi", Element.CRYO, 5, WeaponType.SWORD),
    Character("Raiden Shogun", Element.ELECTRO, 5, WeaponType.POLEARM),
    Character("Razor", Element.ELECTRO, 4, WeaponType.CLAYMORE),
    Character("Rosaria", Element.CRYO, 4, WeaponType.POLEARM),
    Character("Sangonomiya Kokomi", Element.HYDRO, 5, WeaponType.CATALYST),
    Character("Sayu", Element.ANEMO, 4, WeaponType.CLAYMORE),
    Character("Shenhe", Element.CRYO, 5, WeaponType.POLEARM),
    Character("Shikanoin Heizou", Element.ANEMO, 4, WeaponType.CATALYST),
    Character("Sucrose", Element.ANEMO, 4, WeaponType.CATALYST),
    Character("Childe", Element.HYDRO, 5, WeaponType.BOW),
    Character("Thoma", Element.PYRO, 4, WeaponType.POLEARM),
    Character("Traveler", Element.ANEMO, 5, WeaponType.SWORD),
    Character("Traveler", Element.GEO, 5, WeaponType.SWORD),
    Character("Traveler", Element.ELECTRO, 5, WeaponType.SWORD),
    Character("Traveler", Element.DENDRO, 5, WeaponType.SWORD),
    Character("Venti", Element.ANEMO, 5, WeaponType.BOW),
    Character("Wanderer", Element.ANEMO, 5, WeaponType.CATALYST),
    Character("Xiangling", Element.PYRO, 4, WeaponType.POLEARM),
    Character("Xiao", Element.ANEMO, 5, WeaponType.POLEARM),
    Character("Xingqiu", Element.HYDRO, 4, WeaponType.SWORD),
    Character("Xinyan", Element.PYRO, 4, WeaponType.CLAYMORE),
    Character("Yae Miko", Element.ELECTRO, 5, WeaponType.CATALYST),
    Character("Yanfei", Element.PYRO, 4, WeaponType.CATALYST),
    Character("Yaoyao", Element.DENDRO, 4, WeaponType.POLEARM),
    Character("Yelan", Element.HYDRO, 5, WeaponType.BOW),
    Character("Yoimiya", Element.PYRO, 5, WeaponType.BOW),
    Character("Yun Jin", Element.GEO, 4, WeaponType.POLEARM),
    Character("Zhongli", Element.GEO, 5, WeaponType.POLEARM),
]


# Helper functions
def gen_character_dict(
        character: Character, 
        roles: list[str],
        weapons: list[str],
        artifacts: list[str],
        main_stats: list[str],
        sub_stats: list[str],
        talents: list[str],
        tips: list[str],
        notes: str,
    ) -> dict[str, any]:
    return {
        "name": character.name,
        "element": character.element.name,
        "rarity": character.rarity,
        "weapon_type": character.weapon_type.name,
        "roles": roles,
        "weapons": weapons,
        "artifacts": artifacts,
        "main_stats": main_stats,
        "sub_stats": sub_stats,
        "talents": talents,
        "tips": tips,
        "notes": notes,
    }


def save_dict_to_json(dictionary: dict[str, any]):
    file_name = dictionary["name"].lower().replace(" ", "_")
    try:
        with open(os.path.join(dirname, f"cache/{file_name}.json"), "w", encoding="utf-8") as f:
            json.dump(dictionary, f, indent=4)
    except Exception as e:
        print(f"Error saving {file_name} to json: {e}")

def load_json_to_dict(file_name: str) -> dict[str, any]:
    # check if file exists
    if not os.path.isfile(os.path.join(dirname, f"cache/{file_name}.json")):
        return None
    
    with open(os.path.join(dirname, f"cache/{file_name}.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def get_element_url(element: Element):
        return f"https://docs.google.com/spreadsheets/d/{SHEETS_KEY}/export?format=csv&gid={element.get_sheet_id()}"
