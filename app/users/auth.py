from datetime import datetime, timedelta
from typing import Union

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import auth_settings
from app.users.dao import UserDAO
from app.users.schemas import SUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        auth_settings.JWT_SECRET_KEY,
        algorithm=auth_settings.JWT_ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str) -> Union[SUser, None]:
    """Вернет пользователя, если указаны верные email и password,
    None в противном случае."""
    user = await UserDAO.get_one_or_none(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None

    return user
