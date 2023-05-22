from sqlalchemy import delete, exc, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.models import User
from backend.schemas import UserRequest


async def update_user_info(
    session: AsyncSession, user: User, user_info: UserRequest
) -> User | bool:
    for key, value in user_info.dict().items():
        setattr(user, key, value)
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
    except exc.IntegrityError:
        return False
    return user
