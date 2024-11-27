#app/models/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class User_Register(BaseModel):
    fullname: str
    email: EmailStr
    phone_number:int 
    password: str
    conform_password:str

class User_Login(BaseModel):
    email:EmailStr
    password:str

class Car(BaseModel):
    id: int
    name: str
    model: str
    car_number:str
    price_per_day: float
    available: bool

class Booking(BaseModel):
    user_id: int
    car_id: int
    start_date: str
    end_date: str
