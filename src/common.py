from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import os

load_dotenv()
token= os.getenv('TG_BOT_TOKEN')
bot = AsyncTeleBot(token)