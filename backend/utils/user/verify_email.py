from redis.asyncio.client import Redis


async def add_key(redis: Redis, key: str, user_id: str) -> None:
    await redis.set(key, user_id, 60 * 60)


async def verify_key(redis: Redis, key: str) -> str | None:
    return await redis.get(key)
