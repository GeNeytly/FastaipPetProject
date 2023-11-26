from datetime import date
from typing import Optional

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

from app.bookings.router import router as router_booking
from app.users.router import router as router_user


app = FastAPI()

app.include_router(router_booking)
app.include_router(router_user)


class GetHotelsArgs:
    def __init__(
            self,
            location: str,
            date_from: Optional[date] = None,
            date_to: Optional[date] = None,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels/")
def get_hotels(
        search_args: GetHotelsArgs = Depends()
):
    hotels = [
        {
            "address": "Moscow, st. clear, 123",
            "name": "Super hotel",
            "stars": 5
        }
    ]
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


class SBookingResponse(BaseModel):
    room_id: int
    date_from: date
    date_to: date
    status: str


@app.post("/booking/")
def post_hotels(booking: SBooking) -> SBookingResponse:
    response = {
        "room_id": booking.room_id,
        "date_from": booking.date_from,
        "date_to": booking.date_to,
        "status": "OK"
    }
    return response
