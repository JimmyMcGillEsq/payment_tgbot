import os
from datetime import datetime, UTC

from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

# Базовый класс для всех моделей
Base = declarative_base()

class User(Base):
    __tablename__ = 'payment_users'

    telegram_id = Column(BigInteger, primary_key=True) #ID пользователя в Телеграмм
    username = Column(String(50), nullable=True) #username(может быть None, если скрыт)
    first_name = Column(String(50), nullable=False) #имя(обязательное поле)
    last_name = Column(String(50), nullable=True) # фамилия(может быть None)
    phone = Column(String(20), nullable=True) # номер телефона(может быть None)
    is_admin = Column(Boolean, default=False) # админ ли?
    is_active = Column(Boolean, default=True) # Active account?
    registered_at = Column(DateTime(timezone=True), default=datetime.now(tz=UTC)) # registration date

    def __repr__(self):
        return f'<User(id={self.telegram_id}, username="{self.username}")>'

# Создаем синхронный движок SQL
engine = create_engine(
    os.getenv("PAYBOT_DATABASE_URL",'sqlite:///PaymentsBot.db'),
    echo=True)

# Создаем асинхронный движок SQ
AsyncSessionLocal =None
if PAYBOT_ASYNC_DATABASE_URL := os.getenv("PAYBOT_ASYNC_DATABASE_URL"):
    async_engine = create_async_engine(
        os.getenv("PAYBOT_ASYNC_DATABASE_URL","sqlite+aiosqlite:///PaymentsBot.db"),
        echo=True)

#Создание асинхронных сессий для работе с БД
    AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)
