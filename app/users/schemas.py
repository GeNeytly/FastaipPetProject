from pydantic import BaseModel, EmailStr, ConfigDict


class SUserAuth(BaseModel):
    # model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class SUser(BaseModel):
    # model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    hashed_password: str

    class Config:
        from_attributes = True
