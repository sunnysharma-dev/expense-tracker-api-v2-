from pydantic import BaseModel

class UserRegistration(BaseModel):
    username: str
    email: str
    password: str

class CreateExpense(BaseModel):
    title: str
    amount: float
    category: str
