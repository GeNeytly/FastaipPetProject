import os

from dotenv import load_dotenv

load_dotenv()


class DBSettings:
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_NAME: str = os.getenv("DB_NAME")
    DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class AuthSettings:
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")


db_settings = DBSettings()
auth_settings = AuthSettings()
