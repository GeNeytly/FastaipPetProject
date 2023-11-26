from sqlalchemy import (Column, JSON, String,
                        Integer, ForeignKey, Date,
                        Computed)
from app.database import Base
from app.bookings.schemas import SBooking


class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey("rooms.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("(date_to - date_from) * price"))
    total_days = Column(Integer, Computed("date_to - date_from"))

    def to_read_model(self):
        return SBooking(
            id=self.id,
            room_id=self.room_id,
            user_id=self.user_id,
            date_from=self.date_from,
            date_to=self.date_to,
            price=self.price,
            total_cost=self.total_cost,
            total_days=self.total_days
        )
