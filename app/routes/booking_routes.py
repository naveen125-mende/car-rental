#app/routes/booking_routes.py
from fastapi import APIRouter, HTTPException, Depends
from database import cars_collection, users_collection
from models.schemas import Booking
from auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/book", tags=["Booking"], dependencies=[Depends(JWTBearer())])
async def book_car(booking: Booking):
    car = await cars_collection.find_one({"id": booking.car_id})
    user = await users_collection.find_one({"email": users_collection.email})
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not car["available"]:
        raise HTTPException(status_code=400, detail="Car not available")
    booking_data = booking.dict()
    booking_data["status"] = "confirmed"
    await cars_collection.update_one({"id": booking.car_id}, {"$set": {"available": False}})
    return {"message": "Booking confirmed", "booking_details": booking_data}

@router.get("/list", tags=["Booking"], dependencies=[Depends(JWTBearer())])
async def list_bookings():
    return {"message": "List of all bookings"}
