from src.common import bot
from src.dao.models import AsyncSessionLocal, User

# Handle '/start'
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    async with AsyncSessionLocal() as session:
        user =  await session.get(User, message.from_user.id)
        if not user:
            user = User(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name
            )
            session.add(user)
            await session.commit()
            await bot.reply_to(message, 'Вы успешно зарегистрированы')
        else:
            await bot.send_message(message.chat.id, "С возвращением")
