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
    await m.reply_photo(f"https://graph.org/file/6395c7cd3babee3c65ee5.jpg",
        caption="**ʜɪ** 👋\n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ,Ask me any doubt! **\n\n👿 **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[PURPLEBOTZ](https://t.me/purplebotz)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('😎MORE BOTS😍', url='https://t.me/purplebotz')
                    ],  
                    [
                        InlineKeyboardButton("❣️ Admin", url='https://t.me/Lordsakunaa'),
                        InlineKeyboardButton("🤖 Movies", url='https://t.me/+ylvI8ZZcge80MWRl')
                    ]
                ]
            )
        )
  
