from fastapi import APIRouter, Body, Depends, status, HTTPException, Request
from fastapi.responses import StreamingResponse
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient

from backend.database.connection import get_mongo
from backend.utils.user.auth_db import *
from backend.utils.user.business_logic import *
from backend.utils.courses import open_file, get_video_info, check_user_permission
from backend.database.enums import Role

courses_router = APIRouter(tags=["courses"], prefix="/courses")


@courses_router.get(
    "/video",
    response_class=StreamingResponse,
)
async def get_video(
        request: Request,
        course_id: str,
        video_id: str,
        current_user: User = Depends(get_current_user),
        mongo_session: AsyncIOMotorClient = Depends(get_mongo),
        session: AsyncSession = Depends(get_session),
):
    required_score, video_url = await get_video_info(session, mongo_session, course_id, video_id)
    if current_user.role == Role.user.value:
        permission = check_user_permission(current_user, required_score, course_id)
        if not permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have access to this video"
            )
    file, status_code, content_length, headers = await open_file(request, video_url)
    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Video unavailable"
        )
    response = StreamingResponse(
        file,
        media_type='video/mp4',
        status_code=status_code,
    )
    response.headers.update({
        'Accept-Ranges': 'bytes',
        'Content-Length': str(content_length),
        **headers,
    })
    return response


@courses_router.post(
    "/payment",
)
async def pay_by_course(
        course_id: str = Body(),
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_session),
):
    payment = await add_payment(session, current_user, course_id)
    return payment.__dict__
