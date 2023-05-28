from os import environ

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseSettings


class DefaultSettings(BaseSettings):
    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PREFIX")
    APP_HOST: str = environ.get("APP_HOST")
    APP_PORT: int = environ.get("APP_PORT")

    POSTGRES_DB: str = environ.get("POSTGRES_DB")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST")
    POSTGRES_USER: str = environ.get("POSTGRES_USER")
    POSTGRES_PORT: int = environ.get("POSTGRES_PORT")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD")

    REDIS_HOST: str = environ.get("REDIS_HOST")
    REDIS_PORT: int = environ.get("REDIS_PORT")
    REDIS_PASSWORD: str = environ.get("REDIS_PASSWORD")

    MONGO_HOST: str = environ.get("MONGO_HOST")
    MONGO_PASSWORD: str = environ.get("MONGO_PASSWORD")
    MONGO_USER: str = environ.get("MONGO_USER")
    MONGO_PORT: str = environ.get("MONGO_PORT")

    SMTP_SERVER: str = environ.get("SMTP_SERVER")
    SMTP_PORT: int = environ.get("SMTP_PORT")
    SMTP_EMAIL: str = environ.get("SMTP_EMAIL")
    SMTP_PASSWORD: str = environ.get("SMTP_PASSWORD")

    OAUTH2_SCHEME = OAuth2PasswordBearer(
        tokenUrl=f"{APP_HOST}:{APP_PORT}{PATH_PREFIX}/user/auth"
    )

    SECRET_KEY: str = environ.get("SECRET_KEY")
    ALGORITHM: str = environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 1440)
    )

    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @property
    def database_settings(self) -> dict:
        """
        Get all settings for connection with database.
        """
        return {
            "database": self.POSTGRES_DB,
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
        }

    @property
    def database_uri(self) -> str:
        """
        Get uri for connection with database.
        """
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )

    @property
    def database_uri_sync(self) -> str:
        """
        Get uri for connection with database.
        """
        return "postgresql://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )

    @property
    def redis_settings(self) -> dict:
        """
        Get all settings for connection with redis.
        """
        return {
            "password": self.REDIS_PASSWORD,
            "host": self.REDIS_HOST,
            "port": self.REDIS_PORT,
        }

    @property
    def redis_uri(self) -> str:
        """
        Get uri for connection with redis.
        """
        return "redis://:{password}@{host}:{port}".format(
            **self.redis_settings,
        )

    @property
    def mongo_settings(self) -> dict:
        """
        Get all settings for connection with mongo.
        """
        return {
            "user": self.MONGO_USER,
            "password": self.MONGO_PASSWORD,
            "host": self.MONGO_HOST,
            "port": self.MONGO_PORT,
        }

    @property
    def mongo_uri(self) -> str:
        """
        Get uri for connection with mongo.
        """
        return "mongodb://{user}:{password}@{host}:{port}".format(
            **self.mongo_settings,
        )

    class Config:
        env_file = "..env"
        env_file_encoding = "utf-8"
