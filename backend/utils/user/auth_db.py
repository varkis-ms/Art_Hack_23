from sqlalchemy import delete, exc, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.models import User
from backend.schemas import RegistrationFormInDb


async def get_user(session: AsyncSession, email: str) -> User | None:
    query = select(User).where(User.email == email)
    return await session.scalar(query)


async def register_user(
    session: AsyncSession, possible_user: RegistrationFormInDb
) -> bool | User:
    user = User(**possible_user.dict())
    session.add(user)
    try:
        await session.commit()
    except exc.IntegrityError:
        return False
    return user
