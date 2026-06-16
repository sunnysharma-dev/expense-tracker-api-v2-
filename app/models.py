from sqlalchemy import create_engine, Column, Integer, String , DateTime 
from sqlalchemy.orm import sessionmaker, declarative_base
from app.database  import Base
from bcrypt import hashpw, gensalt
from app.database import SessionLocal
from app.auth import PasswordHash
from sqlalchemy import ForeignKey , Float
import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


def new_user(username: str, email: str, password: str):
    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    db = SessionLocal()
    db.add(User(username=username, email=email, hashed_password=hashed_password.decode('utf-8')))
    db.commit()
    db.close()
    return User(username=username, email=email, hashed_password=hashed_password.decode('utf-8'))

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))