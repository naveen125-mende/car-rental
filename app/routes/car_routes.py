#app/routes/car_routes.py
from fastapi import APIRouter, HTTPException
from database import cars_collection
from models.schemas import Car
from fastapi import Depends
from auth.auth_bearer import JWTBearer

router = APIRouter()

@router.get("/list", tags=["cars"])
async def car_list(token: str = Depends(JWTBearer())):
    cars_cursor = cars_collection.find({"available": True})
    cars = await cars_cursor.to_list(length=100)
    if not cars:
        raise HTTPException(status_code=404, detail="No cars available")
    return {"cars": cars}
