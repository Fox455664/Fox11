import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

#writing by teto @G_7_Rr          
                
@app.on_message(filters.command(["السورس","ياسورس","مبرمج السورس","مطور السورس"],""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/06ea0dffac061d340b30a.mp4",
        caption=f"""˛ ❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev¹:𝚗𝚘𝚞𝚛](https://t.me/nor_o)
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev²:𝚊𝚑𝚖𝚎𝚍](https://t.me/F_o_x_5)
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❅✧جـروب الدعـم✧❅", url=f"https://t.me/cr_nox"), 
                 ],[
                   InlineKeyboardButton(
                        "❅✧قــناه الـسورس❅✧", url=f"https://t.me/vzo_a"),
                ],

            ]

        ),

    )
    
