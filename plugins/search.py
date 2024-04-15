
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OPENAI_API, LOG_CHANNEL, AI, UPDATES_CHANNEL
import openai
import asyncio

openai.api_key = OPENAI_API

async def send_message_in_chunks(client, chat_id, text):
    max_length = 4096  # Maximum length of a message
    for i in range(0, len(text), max_length):
        await client.send_message(chat_id, text[i:i + max_length])

@Client.on_message(filters.group | filters.private & filters.text & ~filters.command(['start', 'broadcast']))
async def ai_answer(client, message):
    if AI:
        user_id = message.from_user.id
        if user_id:
            if not await client.get_chat_member(UPDATES_CHANNEL, user_id):
                retry_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Retry", url=f"https://t.me/{UPDATES_CHANNEL}")]])
                await message.reply_text("Please join our updates channel to use this bot.", reply_markup=retry_markup)
                return
            try:
                msg = await message.reply_text("Please wait a moment while the chatbot responds to your query...")
                users_message = message.text
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": users_message}
                    ],
                    max_tokens=1200,
                    temperature=0.6
                )
                footer_credit = "• Report Issue •══• Contact Master •"
                ai_response = response.choices[0].message.content.strip()
                await msg.delete()
                await send_message_in_chunks(client, message.chat.id, f"Here is your answer related to your query 👇\n\n{ai_response}\n\n{footer_credit}")
                await send_message_in_chunks(client, LOG_CHANNEL, f"⭕ A user named: {message.from_user.mention} with user id - {user_id}.\n🔍 asked me this query...👇\n\n🔻 Query: {users_message}\n\n🔻 Here is answer I responded:\n🖍️ {ai_response}\n\n\n🔻 User id:- {user_id} \n🔻 User name:- {message.from_user.mention}")

            except Exception as error:
                print(error)
                await message.reply_text(f"An error occurred:\n\n{error}\n\nForward This Message To @Purpleadmin_dmbot")
    else:
        return
