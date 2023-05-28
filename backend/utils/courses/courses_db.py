from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import exc, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.models_postgres import User, AccessToCourses, Courses


async def add_payment(session: AsyncSession, user: User, course_id: str) -> bool | AccessToCourses:
    payment = AccessToCourses(user_id=user.id, course_id=course_id)
    session.add(payment)
    try:
        await session.commit()
        await session.refresh(payment)
    except exc.IntegrityError:
        return False
    return payment


async def get_video_info_from_mongo(mongo_session: AsyncIOMotorClient,
                                    course_name: str, video_id: str) -> tuple | None:
    mongo_db = mongo_session.courses
    video = await mongo_db[course_name].find_one({"_id": video_id})
    if not video:
        return None
    return video["score"], video["video_url"]


async def get_course_name(session: AsyncSession, course_id: str) -> Courses:
    query = select(Courses).where(Courses.course_id == course_id)
    return await session.scalar(query)
