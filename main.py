import asyncio
import os
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
from src import handlers # NoQa

load_dotenv()
token= os.getenv('TG_BOT_TOKEN')
bot = AsyncTeleBot(token)

if __name__ == '__main__':
    asyncio.run(bot.polling())