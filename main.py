# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Remove-BG-Bot/blob/main/LICENSE

import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

REMOVEBG_API = os.environ.get("REMOVEBG_API", "")
UNSCREEN_API = os.environ.get("UNSCREEN_API", "")
PATH = "./DOWNLOADS/"

FayasNoushad = Client(
    "Remove Background Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
<b>𝗛𝗜 {}, 𝗜 𝗔𝗠 𝗔 𝗕𝗚 𝗥𝗘𝗠𝗢𝗩𝗘𝗥 𝗕𝗢𝗧 𝗜 𝗖𝗔𝗡 𝗘𝗔𝗦𝗜𝗟𝗬 𝗥𝗘𝗠𝗢𝗩𝗘 𝗕𝗔𝗖𝗞𝗚𝗥𝗢𝗨𝗡𝗗 𝗢𝗙 𝗧𝗛𝗘 𝗣𝗜𝗖𝗧𝗨𝗥𝗘𝗦</b>

𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗔𝗡𝗗 𝗠𝗔𝗧𝗜𝗡𝗔𝗘𝗗 𝗕𝗬 @KOT_FREE_DE_LA_HOYA_OFF
"""
HELP_TEXT = """
- Jᴜsᴛ Sᴇɴᴅ Mᴇ ᴀ Pʜᴏᴛᴏ
- I Wɪʟʟ Dᴏᴡɴʟᴏᴀᴅ Iᴛ
- I Wɪʟʟ Sᴇɴᴅ Tʜᴇ Pʜᴏᴛᴏ Wɪᴛʜᴏᴜᴛ Bᴀᴄᴋɢʀᴏᴜɴᴅ

𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗔𝗡𝗗 𝗠𝗔𝗧𝗜𝗡𝗔𝗘𝗗 𝗕𝗬 @KOT_FREE_DE_LA_HOYA_OFF
"""
ABOUT_TEXT = """
╭──────[@KOT_BOTS]───────〄
│
├ Nᴀᴍᴇ : <a href='https://t.me/KOT_BG_REMOVER_BOT'>Kᴏᴛ Bɢ Rᴇᴍᴏᴠᴇʀ Bᴏᴛ</a>
│
├ Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>Hᴇʀᴏᴋᴜ</a>
│ 
├ Lᴀɴɢᴜᴀɢᴇ : <a href='https://docs.pyrogram.org/'>Pʏᴛʜᴏɴ 3.9.6</a>
│
├ Vᴇʀꜱɪᴏɴ : <a href='https://t.me/KOT_BG_REMOVER_BOT</a>
│
├ Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ 1.2.9</a>
│
├ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/KOT_FREE_DE_LA_HOYA_OFF'>✯°• Kᴏᴛ Fʀᴇᴇ Dᴇ Lᴀ Hᴏʏᴀ Oғғ °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪</a>
│
├ Pᴏᴡᴇʀᴇᴅ Bʏ : <a href='https://t.me/KOT_LINKS_TEAM'>Kᴏᴛ Lɪɴᴋs Tᴇᴀᴍ</a>
│
├ Uᴘᴅᴀᴛᴇᴅ Oɴ : [ 19.1.2022 ] 03.00 PM
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('KOT BOTS', url='https://telegram.me/KOT_BOTS'),
        InlineKeyboardButton('SUPPORT GROUP', url='https://telegram.me/KOT_REPORS')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ERROR_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Join Updates Channel', url='https://telegram.me/KOT_BOTS')
        ]]
    )

@FayasNoushad.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@FayasNoushad.on_message(filters.private & (filters.photo | filters.video | filters.document))
async def remove_background(bot, update):
    if not REMOVEBG_API:
        await update.reply_text(
            text="Error :- Remove BG Api is error",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )
        return
    await update.reply_chat_action("typing")
    message = await update.reply_text(
        text="Processing",
        quote=True,
        disable_web_page_preview=True
    )
    if update and update.media:
        new_file = PATH + str(update.from_user.id) + "/"
        if update.photo or (update.document and "image" in update.document.mime_type):
            new_file_name = new_file + "no_bg.png"
            file = await update.download(PATH+str(update.from_user.id))
            await message.edit_text(
                text="Photo downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_image = removebg_image(file)
            if new_image.status_code == 200:
                with open(new_file_name, "wb") as image:
                    image.write(new_image.content)
            else:
                await update.reply_text(
                    text="API is error.",
                    quote=True,
                    reply_markup=ERROR_BUTTONS
                )
                return
            await update.reply_chat_action("upload_photo")
            try:
                await update.reply_document(
                    document=new_file_name,
                    quote=True
                )
                await message.delete()
                try:
                    os.remove(file)
                except:
                    pass
            except Exception as error:
                print(error)
                await message.edit_text(
                    text="Something went wrong! May be API limits.",
                    disable_web_page_preview=True,
                    reply_markup=ERROR_BUTTONS
                ) 
    else:
        await message.edit_text(
            text="Media not supported",
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )


def removebg_image(file):
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(file, "rb")},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVEBG_API}
    )


def removebg_video(file):
    return requests.post(
        "https://api.unscreen.com/v1.0/videos",
        files={"video_file": open(file, "rb")},
        headers={"X-Api-Key": UNSCREEN_API}
    )


FayasNoushad.run()
