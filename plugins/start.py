from pyrogram import Client, filters
from config import LOG_CHANNEL, REACTIONS
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

import telegram
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'BOT_TOKEN'

# Replace 'YOUR_CHANNEL_ID' with your channel ID
CHANNEL_ID = 'purplebotz'

def start(update, context):
    keyboard = [[InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{CHANNEL_ID}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("To receive updates, please join our channel:", reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

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
  
