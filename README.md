# Expense Tracker REST API

A secure backend application built with FastAPI that allows users to register, authenticate, and manage personal expenses.

## Features

* User Registration
* User Login
* Password Hashing using bcrypt
* JWT Authentication
* Protected Routes
* Create Expense
* View Expenses
* Update Expense
* Delete Expense
* Swagger/OpenAPI Documentation

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* JWT
* bcrypt
* Pydantic
* Uvicorn

## API Endpoints

### Authentication

* POST `/register`
* POST `/login`

### Expenses

* POST `/expenses`
* GET `/expenses`
* PUT `/expenses/{expense_id}`
* DELETE `/expenses/{expense_id}`

## Installation

```bash
git clone <repository-url>

cd expense-tracker-api-v2

pip install -r requirements.txt
```

## Run Application

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the server:

```text
http://localhost:8000/docs
```

## Author

Sunny Sharma
