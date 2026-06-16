from fastapi import FastAPI
from app.database import SessionLocal, SessionLocal, engine
from app.database import Base
from app.schemas import UserRegistration
from bcrypt import hashpw, gensalt
from app.models import User
from app.routers import users, expenses
from app.auth import get_current_user

app = FastAPI()

Base.metadata.create_all(bind=engine)




@app.get("/")
def home():

    return {"message": "Welcome to the Expense Tracker API"}

app.include_router(users.router)
app.include_router(expenses.router)


@app.post("/register")
def register_user(user: UserRegistration):
    user = UserRegistration(username=user.username, email=user.email, password=user.password)
    Hashed_password = hashpw(user.password.encode('utf-8'), gensalt())
    db = SessionLocal()
    return {"message": f"User {user.username} registered successfully"} 

