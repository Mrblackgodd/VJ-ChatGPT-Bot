
from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

LOG_TEXT = """#NewUser

ID - {}

Nᴀᴍᴇ - {}
"""


@Client.on_message(filters.command('start'))
async def start_message(c, m):
    user_id = m.from_user.id
    user_name = m.from_user.first_name

    # Check if the user has joined the updates channel
    if not await c.get_chat_member("-1001967167299", user_id):
        await m.reply_text("Please join our updates channel to use this bot.\nhttps://t.me/purplebotz")
        return

    await db.is_user_exist(user_id)
    await db.add_user(user_id, user_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(user_id, m.from_user.mention))
    await m.reply_photo(
        "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg",
        caption="ʜɪ 👋\n\nɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ\n\n⭕ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- Tᴇᴄʜ VJ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://youtube.com/@Tech_VJ')
                ],
                [
                    InlineKeyboardButton("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/Kingvj01'),
                    InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇ", url='https://t.me/VJ_Botz')
                ]
            ]
        )
    )
