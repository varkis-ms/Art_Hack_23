from pathlib import Path

from fastapi import Depends, HTTPException, status
from fastapi.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession
from motor.motor_asyncio import AsyncIOMotorClient

from backend.database.models_postgres import User, AccessToCourses
from backend.utils.courses.courses_db import get_course_name, get_video_info_from_mongo


async def open_file(request: Request, video_url: str) -> tuple:
    path = Path(video_url)
    try:
        file = path.open('rb')
    except:
        return tuple([None] * 4)
    file_size = path.stat().st_size

    content_length = file_size
    status_code = 200
    headers = {}
    content_range = request.headers.get('range')

    if content_range is not None:
        content_range = content_range.strip().lower()
        content_ranges = content_range.split('=')[-1]
        range_start, range_end, *_ = map(str.strip, (content_ranges + '-').split('-'))
        range_start = max(0, int(range_start)) if range_start else 0
        range_end = min(file_size - 1, int(range_end)) if range_end else file_size - 1
        content_length = (range_end - range_start) + 1
        file = ranged(file, start=range_start, end=range_end + 1)
        status_code = 206
        headers['Content-Range'] = f'bytes {range_start}-{range_end}/{file_size}'

    return file, status_code, content_length, headers


def check_user_permission(user: User, score: int, course_id: str) -> bool:
    check_permission = False
    if score > user.score:
        for course in user.permission:
            if AccessToCourses(course).course_id == course_id:
                check_permission = True
                break
    else:
        check_permission = True
    return check_permission


async def get_video_info(session: AsyncSession, mongo_session: AsyncIOMotorClient,
                         course_id: str, video_id: str) -> tuple:
    course_name = await get_course_name(session, course_id)
    if not course_name:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Unknown course_id"
        )
    video_info = await get_video_info_from_mongo(mongo_session, course_name.mongo_name, video_id)
    if not video_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Unknown video_id"
        )
    return video_info[0], video_info[1]
