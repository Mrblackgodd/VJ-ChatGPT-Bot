
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OPENAI_API, LOG_CHANNEL, AI, UPDATES_CHANNEL
import openai
import asyncio

openai.api_key = OPENAI_API

async def send_message_in_chunks(client, chat_id, text):
    max_length = 4096  # Maximum length of a message
    for i in range(0, len(text), max_length):
        await client.send_message(chat_id, text[i:i+max_length])

def generate_join_channel_message():
    message = "Please join our updates channel to use this bot."
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Join Channel", url=UPDATES_CHANNEL)],
        [InlineKeyboardButton("Retry", callback_data="retry")]
    ])
    return message, keyboard

@Client.on_message(filters.group | filters.private & filters.text & ~filters.command(['start', 'broadcast']))
async def ai_answer(client, message):
    if AI == True: 
        user_id = message.from_user.id
        if user_id:
            # Check if user has joined updates channel
            user_channels = await client.get_users(user_id)
            if UPDATES_CHANNEL not in user_channels:
                join_message, join_keyboard = generate_join_channel_message()
                await message.reply_text(join_message, reply_markup=join_keyboard)
                return

            try:
                msg = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ ᴡʜɪʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ ʀᴇsᴘᴏɴᴅs ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ . . .")
                users_message = message.text
                user_id = message.from_user.id
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": users_message}
                    ],
                    max_tokens=1200,  # Increase the value of max_tokens to allow for longer responses
                    temperature=0.6
                )
                footer_credit = "• ʀᴇᴘᴏʀᴛ ɪꜱꜱᴜᴇ •══• ᴄᴏɴᴛᴀᴄᴛ ᴍᴀꜱᴛᴇʀ •"
                ai_response = response.choices[0].message.content.strip()
                await msg.delete()
                await send_message_in_chunks(client, message.chat.id, f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴀɴsᴡᴇʀ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ 👇\n\n{ai_response}\n\n{footer_credit}")
                await send_message_in_chunks(client, LOG_CHANNEL, f"⭕ ᴀ ᴜsᴇʀ ɴᴀᴍᴇᴅ: {message.from_user.mention} ᴡɪᴛʜ ᴜsᴇʀ ɪᴅ - {user_id}.\n🔍 ᴀsᴋᴇᴅ ᴍᴇ ᴛʜɪs ǫᴜᴇʀʏ...👇\n\n🔻 ǫᴜᴇʀʏ: {users_message}\n\n🔻 ʜᴇʀᴇ ɪs ᴀɴsᴡᴇʀ ɪ ʀᴇsᴘᴏɴᴇᴅ:\n🖍️ {ai_response}\n\n\n🔻 ᴜsᴇʀ ɪᴅ :- {user_id} \n🔻 ᴜsᴇʀ ɴᴀᴍᴇ :- {message.from_user.mention}")
                
            except Exception as error:
                print(error)
                await message.reply_text(f"An error occurred:\n\n{error}\n\nForward This Message To @Purpleadmin_dmbot")
    else:
        return
