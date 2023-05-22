from sqlalchemy import delete, exc, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.models import AuthTablePassword, User
from backend.schemas import RegistrationFormInDb


async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    query = select(User).where(User.email == email)
    return await session.scalar(query)


async def get_user_by_id(session: AsyncSession, user_id: str) -> User | None:
    query = select(User).where(User.id == user_id)
    return await session.scalar(query)


async def register_user(
    session: AsyncSession, possible_user: RegistrationFormInDb
) -> bool | User:
    user = User(email=possible_user.email)
    user.password = AuthTablePassword(password=possible_user.password)
    session.add(user)
    try:
        await session.commit()
    except exc.IntegrityError:
        return False
    return user
