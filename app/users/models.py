from sqlalchemy import Column, Integer, String

from app.database import Base
from app.users.schemas import SUser


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    def to_read_model(self):
        return SUser(
            id=self.id,
            email=self.email,
            hashed_password=self.hashed_password
        )
