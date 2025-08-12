import asyncio
from src.common import bot
#import handlers for telebot
from src import handlers # NoQa

if __name__ == '__main__':
    asyncio.run(bot.polling())