from pyrogram import Client, filters
from config import LOG_CHANNEL, REACTIONS
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
    updates_channel = "https://t.me/purplebotz"

    # Check if the user has joined the updates channel
    if not await c.get_chat_member(updates_channel, m.from_user.id):
        await m.reply_text("Please join our updates channel to use this bot.")
        return

    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    
    # Send the welcome message
    await m.reply_photo("https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg",
        caption="ʜɪ 👋\n\nɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ\n\n⭕ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- [PURPLEBOTZ](https://t.me/purplebotz)",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💝 Movies', url='https://t.me/+ylvI8ZZcge80MWRl')
                    ],  
                    [
                        InlineKeyboardButton("❣️ ADMIN", url='https://t.me/Lordsakunaa'),
                        InlineKeyboardButton("🤖 MORE BOTS", url='https://t.me/purplebotz')
                    ]
                ]
            )
    )
