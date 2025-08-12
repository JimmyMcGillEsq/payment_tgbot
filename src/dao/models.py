from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime, UTC

# базовый класс.
Base = declarative_base()

class User(Base):
    __tablename__ = 'payment_users'

    telegram_id = Column(Integer, primary_key=True) #ID пользователя в Телеграмм
    username = Column(String(50), nullable=True) #username(может быть None, если скрыт)
    first_name = Column(String(50), nullable=False) #имя(обязательное поле)
    last_name = Column(String(50), nullable=True) # фамилия(может быть None)
    phone = Column(String(20), nullable=True) # номер телефона(может быть None)
    is_admin = Column(Boolean, default=False) # админ ли?
    is_active = Column(Boolean, default=True) # Active account?
    registered_at = Column(DateTime, default=datetime.now(tz=UTC)) # registration date

def __repr__(self):
        return f'<User(id={self.telegram_id}, username="{self.username}")>'
engine = create_engine(
    os.getenv("PAYBOT_DATABASE_URL",'sqlite:///PaymentsBot.db'),
    echo=True)