from typing import List, Dict

from fastapi import APIRouter, HTTPException, status, Response

from app.users.schemas import SUserAuth
from app.users.dao import UserDAO
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.schemas import SUser


router = APIRouter(
    prefix="/users",
    tags=["Auth & Users"]
)


@router.get("/")
async def get_all_users() -> List[SUser]:
    users = await UserDAO.get_all()
    return users


@router.post("/register")
async def register_user(user_data: SUserAuth) -> None:
    existing_user = await UserDAO.get_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists!"
        )
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth) -> Dict[str, str]:
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not correct email or password!"
        )
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}
