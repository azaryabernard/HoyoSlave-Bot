""" LINKS UTILITY """
from discord import Embed

""" Genshin Impact Links and Embeds """
# Genshin Impact Interactive Map
gi_hoyolab_map = 'https://act.hoyolab.com/ys/app/interactive-map/index.html?lang=en-us#/map/'
gi_hoyolab_map_icon = "https://static.wikia.nocookie.net/logopedia/images/3/33/HoYoLAB_icon_new.png/revision/latest/scale-to-width-down/250?cb=20220530005712"
gi_app_sample = 'https://genshin-impact-map.appsample.com/'
gi_app_sample_icon = "https://gim.appsample.net/images/share.jpg"

EMBEDS_MAP_LINKS = [
    Embed(title='HoYoLAB Genshin Impact Interactive Map', url=gi_hoyolab_map, color=0x00ff00).set_thumbnail(url=gi_hoyolab_map_icon), 
    Embed(title='AppSample Genshin Impact Interactive Map', url=gi_app_sample,  color=0x00ff00).set_thumbnail(url=gi_app_sample_icon)
]


# Genshin Impact Wiki
gi_wiki = 'https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki'

EMBEDS_WIKI_LINKS = [
    Embed(title='Genshin Impact Wiki', url=gi_wiki, color=0x00ff00).set_thumbnail(url="https://ih1.redbubble.net/image.1788133237.8111/st,small,845x845-pad,1000x1000,f8f8f8.jpg")
]


# Genshin Impact Database
paimon_moe = 'https://paimon.moe/'
paimon_moe_icon = 'https://paimon.moe/images/paimon_hello.png'
ambr_top = 'https://ambr.top/en'
ambr_top_icon = 'https://ambr.top/images/icon.png'

EMBEDS_DB_LINKS = [
    Embed(title="Paimon Moe", url=paimon_moe, color=0x00ff00).set_thumbnail(url=paimon_moe_icon),
    Embed(title='Project Amber', url=ambr_top, color=0x00ff00).set_thumbnail(url=ambr_top_icon)
]


# Genshin Impact TC, Character Builds, and Guides
helper_team = 'https://docs.google.com/spreadsheets/d/1gNxZ2xab1J6o1TuNVWMeLOZ7TPOqrsf3SshP5DLvKzI/'
helper_team_icon = 'https://lh3.googleusercontent.com/u/0/docs/ADP-6oEPMDeWOhG_eV5QDxJRsoWD4Syj2iGHiwHkDitFokeIME2Q03raHu8Yn8lVGSkQ_uaPEwGw6_sxc5j_tvFnpYT8AmXoh01hgIx7xorCjputU_c0Z4DycZXCI40ydHv7WZJOYUvCLqx9BSy1Gjk34bjDwlOUAyYQk8UCI9nXGT3aVizzBfYVskmlRyLmo7_TZeSgozQSS8YHuJnsfpMDQ8tJy6ZmsG0bR6dd9pfolIADAmhOoykMbtkmVEnGJIiautB7pIs8qVCmWBpvid6UvR4roBiT5Lb684HRKP-ouba4or6yShq0E0UW4fcnlDHFBkAYqdk9FsH5yVUWJsw-engjkYkuOx4xTvEdW8FnLjGdVJhQ8f0xDQv0ghPFXXCdhPrq2e2dmBJT6e-Xav322lrBMIIIUrF_fIVx2_MOCWWpL1XlZVeaSVBFcKJkBufjQU1uzckejoxJu1dwZedhddQVzrBgJgCCr0OF6Ya-SWpOAtffW5lk71Dh9E-C5fdIPtnQqQFKIPjJAitVhilit3fcqFCoynWQSSmJkoqdZl1N7ScPqvlBoBXggyMCXayeF1FdhjL-0p3aKd7SVS0iQXQF5VTCJRU_P-_N6pBE4fa949Kmo3X6tGGsntME8upghXLHHkvD-ZXulB4wAdGi_aEsp1hU0bVuWYT7aXYFQy6RWw2FX8l6o3oNBcZY-zXsPJaUAx5YAXwXYVRcVgl6rogVkfr0SWfnO8OGDiCK0jufzMciWYx_kUWlYJkRKsZyLEIG1Ey9aY9FDhBY_RmI3hvSI4ZmjNCY3T3xa8wQvlV_6anQSSd0DoUv_tq-gWU-wpX7YVsGjPtF4W6fqBI32NPk5Lqs1GFRkGgkFCmScQfaJazs6E4gCCLr60go--5GndSqRcsX5GjwK6jnPdPFOMV0hg94uDsSlBiZqaU9ZznxDFC9BSLe0NuQAxSSyDjV0uuO6f67xCJG1Tmp3nMs4KG0fbOPttDXla-nPvQQSg0nXE4Gb-kbG6d8qWQuiKJ1n1-bXBp9XafUpSsm7IcyFUj_rXzRpROQFf9FFxPn5oxAfH9WJQLwDdACNsh1=w851-h474'
base_stat_comp = 'https://genshin-impact.fandom.com/wiki/Character/Comparison'
base_stat_icon = "https://ih1.redbubble.net/image.1788133237.8111/st,small,845x845-pad,1000x1000,f8f8f8.jpg"
kqm = 'https://keqingmains.com'
kqm_icon = 'https://keqingmains.com/wp-content/uploads/2021/10/kqm-logo-full-e1633177025729.png'

EMBEDS_BUILD_LINKS = [
    Embed(title='Helper Team\'s Characters Builds', url=helper_team, color=0x00ff00).set_thumbnail(url=helper_team_icon),
    Embed(title='Base Stat Comparison', url=base_stat_comp, color=0x00ff00).set_thumbnail(url=base_stat_icon),
    Embed(title='KeqingMains', url=kqm, color=0x00ff00).set_thumbnail(url=kqm_icon)
]

# Honkai: Star Rail Map
star_rail_map = 'https://act.hoyolab.com/sr/app/interactive-map/index.html?lang=en-us#/map/'
star_rail_map_icon = 'https://static.wikia.nocookie.net/logopedia/images/3/33/HoYoLAB_icon_new.png/revision/latest/scale-to-width-down/250?cb=20220530005712'

EMBEDS_HSR_MAP_LINKS = [
    Embed(title='Star Rail Map', url=star_rail_map, color=0x00ff00).set_thumbnail(url=star_rail_map_icon)
]