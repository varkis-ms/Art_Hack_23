from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.models_postgres import User
from backend.schemas import UserInfo


async def update_user_info(
        session: AsyncSession, user: User, user_info: UserInfo
) -> User | bool:
    for key, value in user_info.dict().items():
        if value:
            setattr(user, key, value)
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
    except exc.IntegrityError:
        return False
    return user
