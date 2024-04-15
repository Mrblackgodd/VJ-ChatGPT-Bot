
from pyrogram import Client, filters
from config import LOG_CHANNEL, UPDATES_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

LOG_TEXT = """#NewUser

ID - {}

Nᴀᴍᴇ - {}"""

@Client.on_message(filters.command('start') & filters.private)
async def start_message(c, m):
    if await c.get_chat_member(UPDATES_CHANNEL, m.from_user.id):
        await db.is_user_exist(m.from_user.id)
        await db.add_user(m.from_user.id, m.from_user.first_name)
        await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
        await m.reply_photo("https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg",
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
    else:
        await m.reply_text("Please join our updates channel to use this bot.", reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{UPDATES_CHANNEL}")]
            ]
        ))

@Client.on_inline_query()
async def button_click(c, q):
    if q.data == "retry":
        if await c.get_chat_member(UPDATES_CHANNEL, q.from_user.id):
            await q.answer(text="You have successfully joined the updates channel!")
        else:
            await q.answer(text="Please join the updates channel to use this bot.", show_alert=True)
