#app/routes/car_routes.py
from fastapi import APIRouter, HTTPException
from database import cars_collection,admins_collection
from models.schemas import Car
from fastapi import Depends 
from auth.auth_bearer import JWTBearer
router = APIRouter()
@router.post('/adding/',tags=["cars"])
async def add_car(car:Car,token: str = Depends(JWTBearer())):
    email = token.find("email")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

    admin = await admins_collection.find_one({"email": email})  
    if not admin:
        raise HTTPException(status_code=400, detail="Admin not found")
    
    car_dict = car.dict()
    await cars_collection.insert_one(car_dict)
    
    return {"message": "Successfully added the car", "car": car_dict}


    
