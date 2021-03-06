#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        

                [InlineKeyboardButton("๐ถ๐พ๐ค๐ข๐ข๐๐ฃ๐๐จ๐ค", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "โค๏ธ๐พโ๐๐โ๐ค", url=f"https://t.me/Urban_Chat_Group"

                    ),

                    InlineKeyboardButton(

                        "โค๏ธ๐พ๐๐ฝ๐ด๐๐ค", url=f"https://t.me/PB_65_Aujla"

                    ),

                ],
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [

                    InlineKeyboardButton(

                        "๐ ๐ผ๐ฟ๐ฟ ๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐ค",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("๐ถ๐พ๐ค๐ข๐ข๐๐ฃ๐๐จ๐ค", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "๐๐แดsแดษดแดษช แดสแดแด๐", url=f"https://t.me/Urban_Chat_Group"

                    ),

                    InlineKeyboardButton(

                        "๐ฅ๐ข๐ฅ๐๐ฅ๐ฆ๐ค๐ฅ", url=f"https://t.me/Punjabi_Status_Mania"

                    ),

                ],
        [InlineKeyboardButton("๐ฎ๐ณ ๐๐๐ฃ๐๐ช๐๐๐ ๐", callback_data="LG")],
    ]
  
    return buttons
