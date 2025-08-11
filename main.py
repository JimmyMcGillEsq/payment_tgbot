import asyncio
import os
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv

load_dotenv()
token= os.getenv('TG_BOT_TOKEN')
bot = AsyncTeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

if __name__ == '__main__':
    asyncio.run(bot.polling())