from app.models import Expense
from app.schemas import CreateExpense
from fastapi import APIRouter
from app.database import SessionLocal
from fastapi import Depends
from app.auth import get_current_user


router = APIRouter()

@router.post("/expenses")
def create_expense(expense: CreateExpense, current_user: dict = Depends(get_current_user)):
    try:
        db = SessionLocal()
        db_expense = Expense(title=expense.title, amount=expense.amount, category=expense.category, user_id=current_user["user_id"])
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        return {"message": f"Expense '{expense.title}' created successfully", "expense": db_expense}
    finally:
        db.close()    

@router.get("/expenses")
def get_expenses(current_user: dict = Depends(get_current_user)):
    try:
        db = SessionLocal()
        expenses = db.query(Expense).filter(Expense.user_id == current_user["user_id"]).all()
        return {"expenses": expenses}
    finally:
        db.close()        

@router.put("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: CreateExpense, current_user: dict = Depends(get_current_user)):
    try:
        db = SessionLocal()
        db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if not db_expense:
            return {"message": "Expense not found"}
        if db_expense.user_id != current_user["user_id"]:
            return {"message": "Unauthorized"}
        db_expense.title = expense.title
        db_expense.amount = expense.amount
        db_expense.category = expense.category
        db.commit()
        db.refresh(db_expense)
        return {"message": f"Expense '{expense.title}' updated successfully", "expense": db_expense}
    finally:
        db.close()

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int , current_user: dict = Depends(get_current_user)):
    try:
        db = SessionLocal()
        db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if not db_expense:
            return {"message": "Expense not found"}
        if db_expense.user_id != current_user["user_id"]:
            return {"message": "Unauthorized"}
        db.delete(db_expense)
        db.commit()
        return {"message": f"Expense '{db_expense.title}' deleted successfully"}
    finally:
        db.close()