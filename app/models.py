from pydantic import BaseModel
from datetime import date

class Transaction(BaseModel):
    id: int
    date: date
    sales: int

class User(BaseModel):
    id: int
    signup_date: date
