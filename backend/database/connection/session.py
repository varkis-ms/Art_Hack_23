from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import redis.asyncio as redis
from redis.asyncio.client import Redis
from motor.motor_asyncio import AsyncIOMotorClient

from backend.config import get_settings


class SessionManager:
    def __init__(self) -> None:
        self.refresh()

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SessionManager, cls).__new__(cls)
        return cls.instance  # noqa

    def get_session_maker(self) -> sessionmaker:
        return sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

    def refresh(self) -> None:
        self.engine = create_async_engine(
            get_settings().database_uri, echo=True, future=True
        )


async def get_session() -> AsyncSession:
    session_maker = SessionManager().get_session_maker()
    async with session_maker() as session:
        yield session


async def get_redis() -> Redis:
    return redis.from_url(get_settings().redis_uri, decode_responses=True)


async def get_mongo() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(get_settings().mongo_uri)


__all__ = [
    "get_session",
    "get_redis",
    "get_mongo",
]
