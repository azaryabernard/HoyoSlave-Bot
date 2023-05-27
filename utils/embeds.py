""" LINKS UTILITY """
from discord import Embed

""" Genshin Impact Links and Embeds """
# Genshin Impact Interactive Map
gi_hoyolab_map = 'https://act.hoyolab.com/ys/app/interactive-map/index.html?lang=en-us#/map/'
gi_hoyolab_map_icon = "https://static.wikia.nocookie.net/logopedia/images/3/33/HoYoLAB_icon_new.png/revision/latest/scale-to-width-down/250?cb=20220530005712"
gi_app_sample = 'https://genshin-impact-map.appsample.com/'
gi_app_sample_icon = "https://gim.appsample.net/images/share.jpg"

EMBEDS_GI_MAP_LINKS = [
    Embed(title='HoYoLAB Genshin Impact Interactive Map', url=gi_hoyolab_map, color=0x00ff00).set_thumbnail(url=gi_hoyolab_map_icon), 
    Embed(title='AppSample Genshin Impact Interactive Map', url=gi_app_sample,  color=0x00ff00).set_thumbnail(url=gi_app_sample_icon)
]


# Genshin Impact Wiki
gi_wiki = 'https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki'

EMBEDS_GI_WIKI_LINKS = [
    Embed(title='Genshin Impact Wiki', url=gi_wiki, color=0x00ff00).set_thumbnail(url="https://ih1.redbubble.net/image.1788133237.8111/st,small,845x845-pad,1000x1000,f8f8f8.jpg")
]


# Genshin Impact Database
paimon_moe = 'https://paimon.moe/'
paimon_moe_icon = 'https://paimon.moe/images/paimon_hello.png'
ambr_top = 'https://ambr.top/en'
ambr_top_icon = 'https://ambr.top/images/icon.png'

EMBEDS_GI_DB_LINKS = [
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

EMBEDS_GI_BUILD_LINKS = [
    Embed(title='Helper Team\'s Characters Builds', url=helper_team, color=0x00ff00).set_thumbnail(url=helper_team_icon),
    Embed(title='Base Stat Comparison', url=base_stat_comp, color=0x00ff00).set_thumbnail(url=base_stat_icon),
    Embed(title='KeqingMains', url=kqm, color=0x00ff00).set_thumbnail(url=kqm_icon)
]

# HSR Impact Wiki
hsr_wiki = 'https://honkai-star-rail.fandom.com/wiki/Honkai:_Star_Rail_Wiki'
hsr_wiki_icon = "https://play-lh.googleusercontent.com/AsaeL9oWkGdjyDNwbmzsaYY_WxdPrmQVGUfgfzL4mhJteC1X3HdLib9bafnXaYr3WB8=w240-h480-rw"

EMBEDS_HSR_WIKI_LINKS = [
    Embed(title='Honkai: Star Rail Wiki', url=hsr_wiki, color=0x00ff00).set_thumbnail(url=hsr_wiki_icon)
]

# Honkai: Star Rail Map
hsr_map = 'https://act.hoyolab.com/sr/app/interactive-map/index.html?lang=en-us#/map/'
hsr_map_icon = 'https://static.wikia.nocookie.net/logopedia/images/3/33/HoYoLAB_icon_new.png/revision/latest/scale-to-width-down/250?cb=20220530005712'

EMBEDS_HSR_MAP_LINKS = [
    Embed(title='Star Rail Map', url=hsr_map, color=0x00ff00).set_thumbnail(url=hsr_map_icon)
]

# Honkai: Star Rail TC, Character Builds, and Guides
hsr_helper_team = 'https://docs.google.com/spreadsheets/d/1FG_6viMaygymJucNU60pGptbgDjLNOpUKPD81pZQ1_Y'
hsr_helper_team_icon = "https://lh3.googleusercontent.com/fife/APg5EObrK_J0SbnPMXuEVGn00boDwvnm1r00grQC9sTIk2PahBHvfs-5CGg26oP7AzaNrZA5MRs-o6igd0GyVVmt5YLoxVqOKNvLsWmJUlYbyglrNWplvKLnLcg6sTPr1vaVmcluA6icmBhlM3tCRbMDWjJL7wzJTp-ehMRccO6n8tjYSmvBlnx5IEy2ralyWoC1Ex7T0tDCsBv7RurXN9jaLCnhGkHJIUSgvvfevvt1TEj1rIlal_zSyBrGkgC9TxbaW19Fd8uJto9k1WjY6KPP5UTfA0DJXqj_SPphpaAhU__Vb2Fcs73dRddinG0LjVeJFf8eGKK23stkUB__72eXUdwJLwvOhtpvOLmLPGt4kwxqHqC836U_lisel-5E4ZzIxlHacLsCrJa5L1YK-weKs_36mbjkAyTV4NXE4M08qWHQQyGY00T5piNwr1lJPDjYZMQhv0VZw-uj5qopYr9XfJu4_D3kTqHGrV8Sl84UBCvztbhc2prK1KAcoRNH_l_1yhXLywjd9dG0ox19DkthMVoEsdw9ug-X1_YwI63sgik7DLK4S4JulYChvh4iFe40ZDnu-LFiFLJ1wJ6m3GKxPXIsCM0vEJ1ujm8ZT_Ok8uSQ1HP9KalbobiVem9nCJzKNHbBEE4syBCriAq3AHPVCrmcabBmvkxvonJXKyRRSwwU5eITWF_Wey_6UlE4gdgEnYah3HJ2u8hI23FTjDoPO1gJDhSokhrcO7AtRQiV7l_LqTHlPDQMUiVCnt42U8nheM-7cpVrwd0QawBA2M4cVeNLRLlr3XeOND2mp1InpkrOMDxkPgISlXi6dJGuJsAZgj2joIVSs2Di-azpwieCncZx50ZXDRh6kCLxlO2Yo4z77uhbJx2vkfRs02JGmufNtFfKAg_BYE-vIM5H325jZSc19mQHrvkjbrEMdO8kDeLRYZ4u99jQUgceWk9-Lm29FdHXFvOwfzBuB2QM_tNvNt_ZdcvikrKonU0g6caZ509SchtwfFM3UU4Qna22CXzvdkgVAYLbyWYa3Uq-2egcqw11uCQlh9x5-EesCA3XRlKn1ZbriBAO2ZvzS2rt93ECTndwRyvhfBFY0dAXJ0bY6quraC4BOBXRmOJD53RLtH-EfiPMOqk7O31-26h-h38WYOnug9jtiJkg2R1OMel-KCvX_ts0OoG2CpzKor7KWI-XX1XpualdZ2ZMZjUGRuZ8Z-BPc80yiU3qiUNEE8Gf8oqJw81yPk3Ih2kf4oQA7b7ytzwmjWek1O2c2gqKaDO5wCLXx9QyXP452Np1kUSMBAQ6PStYk2MqBsaktfMlmb7RMDX_VYwCT7kcTEO_fMcHfXP2PfjSTTOwMDZjAtf1sYSwS8vMQlzvcasFL8XOeKQM5LYapXzcOBAxAKyTg8GYmqCgFZLK5glhnnykLcdnLdIShNB9SQmL6ryVCkSxJFwUL-dlqxMOIody5QzXWcbxcAr14gvqnt9R2OecusVOOejq98z9YQ0u63ZyRr-_s1XO5Y4vGkdvPDwnO4yF1yyBOzAWCrEEpn92EtpG3v_GxW2HWv9H3pvUN9yXwA=w3456-h1896"

EMBEDS_HSR_BUILD_LINKS = [
    Embed(title='Helper Team\'s Characters Builds', url=hsr_helper_team, color=0x00ff00).set_thumbnail(url=hsr_helper_team_icon)
]

# Honkai: Star Rail Database
hsr_prydwen = 'https://www.prydwen.gg/star-rail/'
hsr_prydwen_icon = 'https://www.prydwen.gg/static/e5cca805ee22a6a5327c633bbab70f48/c5628/prydwen_logo_small.webp'
hsr_starrailstation = 'https://starrailstation.com/en'
hsr_starrailstation_icon = 'https://starrailstation.com/9437f709e7dcd20c41dfd76f66de2def.png'

EMBEDS_HSR_DB_LINKS = [
    Embed(title='Prydwen\'s Star Rail Database', url=hsr_prydwen, color=0x00ff00).set_thumbnail(url=hsr_prydwen_icon),
    Embed(title='Star Rail Station', url=hsr_starrailstation, color=0x00ff00).set_thumbnail(url=hsr_starrailstation_icon)
]

# Error Messages