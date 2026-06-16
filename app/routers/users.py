import email

from app.schemas import UserRegistration
from fastapi import APIRouter
from app.database import SessionLocal
from app.models import User
from app.auth import PasswordHash
import bcrypt
from fastapi import Depends , HTTPException, status
from app.auth import get_current_user , create_token
import datetime
import os
from dotenv import load_dotenv
from app.schemas import CreateExpense
from app.models import Expense




load_dotenv()




router = APIRouter()

@router.post("/register")
def register_user(user: UserRegistration):
    
    hashed_password = PasswordHash(user.password)
    try :
        db = SessionLocal()
        email_exists = db.query(User).filter(User.email == user.email).first()
        if email_exists:
            return {"message": "Email already exists"}
        db.add(User(username=user.username, email=user.email, hashed_password=hashed_password))
        db.commit()
        return {"message": f"User {user.username} registered successfully"}
    finally:
        db.close()   

@router.post("/login")
def login_user(email:str , password:str):
    try:
        db = SessionLocal()
        db_user = db.query(User).filter(User.email == email).first()
        if not db_user:
            return {"message": "Invalid email or password"}
        if bcrypt.checkpw(password.encode('utf-8'), db_user.hashed_password.encode('utf-8')):
            return {"message": f"User {db_user.username} logged in successfully"}
        else:
            return {"message": "Invalid email or password"}
    finally:        db.close()

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm="HS256")
    return encoded_jwt

    
                    