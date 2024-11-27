#app/routes/admins.py
from fastapi import APIRouter, HTTPException
from database import admins_collection
from auth.auth_handler import signJWT
from models.schemas import User_Register,User_Login
import bcrypt

router = APIRouter()

@router.put("/register", tags=["Admins"])
async def register(user: User_Register):
    cur_user = await admins_collection.find_one({"email": user.email})
    if cur_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    user_dict = user.dict()
    user_dict["password"] = hashed_password.decode("utf-8") 
    await admins_collection.insert_one(user_dict)
    return {"message": "User registered successfully"}

@router.post("/login", tags=["Admins"])
async def login(user: User_Login):
    
    stored_user = await admins_collection.find_one({"email": user.email})
    if not stored_user:
        raise HTTPException(status_code=400, detail="Invalid email")

    stored_password = admins_collection["user"]
    if not bcrypt.checkpw(user.password.encode("utf-8"), stored_user["password"].encode("utf-8")):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = signJWT({"email":user.email})
    return {"access_token": token}
    print("token generated")
