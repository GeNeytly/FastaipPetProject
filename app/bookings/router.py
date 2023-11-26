from typing import List, Union
from pprint import pprint

from fastapi import APIRouter

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("/")
async def get_bookings() -> List[SBooking]:
    return await BookingsDAO.get_all()


@router.get("/filtered")
async def get_filtered_bookings(room_id: int) -> List[SBooking]:
    return await BookingsDAO.get_filtered(room_id=room_id)


@router.get("/{id}")
async def get_by_id(id: int) -> Union[SBooking, None]:
    return await BookingsDAO.get_one_or_none(id=id)
