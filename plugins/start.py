from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUsergpt
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg",
        caption="**ʜɪ** 👋\n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[𝐏𝐔𝐑𝐏𝐋𝐄 𝐁𝐎𝐓𝐙](https://t.me/purpleebots)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🎥Movies/Webseries Search Group💕', url='https://t.me/+ylvI8ZZcge80MWRl')
                    ],  
                    [
                        InlineKeyboardButton("🥊𝐌𝐎𝐑𝐄 𝐁𝐎𝐓𝐒🥊", url='https://t.me/ezpzsupport/17'),
                        InlineKeyboardButton("😍Anime😍", url='https://t.me/+nKz9rQJ893BlMGRl')
                    ]
                ]
            )
        )
  
