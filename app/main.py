from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.admins import router as admins_router
from routes.users_routes import router as users_router
from routes.car_routes import router as car_router
from routes.booking_routes import router as booking_router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(admins_router, prefix="/api/admins")
app.include_router(users_router, prefix="/api/users")
app.include_router(car_router, prefix="/api/cars")
app.include_router(booking_router, prefix="/api/bookings")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Car Rental API is running successfully!"}
