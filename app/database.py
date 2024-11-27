#app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL")
client = AsyncIOMotorClient(MONGODB_URL)
db = client["Car_rental"]
users_collection = db["users"]
admins_collection = db["admins"]
cars_collection = db["cars"]
print("mongodb connected")
