#app/models/schemas.py
from pydantic import BaseModel, EmailStr,validator,Field
from typing import Optional

class User_Register(BaseModel):
    full_name: str = Field(..., max_length=50)
    email: EmailStr
    phone_number:int 
    password: str
    conform_password:str

    @validator('full_name')
    def validate_full_name(cls,value):
        if not value.isalpha()  and ' ' not in value:
            raise ValueError ('Full name must contain only alphabetic characters and spaces.')
        if len(value) == 0:
            raise ValueError("full name can not be blank")
        return value 
    
    @validator('email')
    def validate_email(cls,value):
        if len(value) == 0:
            raise ValueError("email can not be blank")
        return value

class User_Login(BaseModel):
    email:EmailStr
    password:str

class Car(BaseModel):
    car_name: str
    model: str
    car_number:str
    price_per_day: float
    available: bool 
    no_of_seaters:int 

class Booking(BaseModel):
    user_email: EmailStr
    car_id: int
    start_date: str
    end_date: str
