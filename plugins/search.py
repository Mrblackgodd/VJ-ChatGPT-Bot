
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OPENAI_API, LOG_CHANNEL, AI, UPDATES_CHANNEL
import openai
import asyncio

openai.api_key = OPENAI_API

async def send_message_in_chunks(client, chat_id, text):
    max_length = 4096  # Maximum length of a message
    for i in range(0, len(text), max_length):
        await client.send_message(chat_id, text[i:i+max_length])

@Client.on_message(filters.group | filters.private & filters.text & ~filters.command(['start', 'broadcast']))
async def ai_answer(client, message):
    if AI:
        user_id = message.from_user.id
        if user_id:
            if not await client.get_chat_member(UPDATES_CHANNEL, user_id):
                join_message = "Please join our Updates Channel to use this bot."
                join_button = InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton("Join Updates Channel", url=f"t.me/{UPDATES_CHANNEL}")]]
                )
                await message.reply_text(join_message, reply_markup=join_button)
                return

            try:
                msg = await message.reply_text("Please wait while the chatbot responds to your query...")
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
                await send_message_in_chunks(client, LOG_CHANNEL, f"A user named: {message.from_user.mention} with user id - {user_id}.\nAsked me this query...👇\n\n🔻 Query: {users_message}\n\n🔻 Here is answer I responded:\n🖍️ {ai_response}\n\n\n🔻 User ID: {user_id}\n🔻 User Name: {message.from_user.mention}")

            except Exception as error:
                print(error)
                await message.reply_text(f"An error occurred:\n\n{error}\n\nForward This Message To @Purpleadmin_dmbot")
    else:
        return

@Client.on_callback_query(filters.regex("verify_channel"))
async def verify_channel(client, callback_query):
    user_id = callback_query.from_user.id
    if await client.get_chat_member(UPDATES_CHANNEL, user_id):
        await callback_query.answer("You have successfully verified the channel.")
        await callback_query.message.delete()
        await ai_answer(client, callback_query.message)
    else:
        await callback_query.answer("Please join the Updates Channel to verify.")
