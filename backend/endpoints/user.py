from uuid import uuid4

from fastapi import APIRouter, Body, Depends, status, Path, BackgroundTasks, HTTPException
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.models_postgres import User
from backend.schemas import UserRequest, UserSchema, UserInfo, UserEmail
from backend.utils.user.business_logic import get_current_user, get_session
from backend.utils.user.user_db import update_user_info
from backend.utils.user.auth_db import get_user_by_id
from backend.utils.user import add_key, verify_key, verify_email
from backend.database.connection import get_redis

user_router = APIRouter(tags=["user"], prefix="/user")


@user_router.patch(
    "/update",
    response_model=UserSchema,
)
async def update_info_about_user(
        update_form: UserRequest = Body(),
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_session),
):
    user = await update_user_info(session, current_user, UserInfo(**update_form.dict()))
    if user:
        return UserSchema.from_orm(user)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Login already exists.",
    )


@user_router.get(
    "/verify/{key}",
)
async def check_verify_email(
        key: str = Path(),
        session: AsyncSession = Depends(get_session),
        redis: Redis = Depends(get_redis),
):
    user_id = await verify_key(redis, key)
    if user_id:
        current_user = await get_user_by_id(session, user_id)
        user = await update_user_info(session, current_user, UserInfo(email_verified=True))
        return {"message": f"Successful confirmed email {user.email}."}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Unknown key for confirmation email.",
    )


@user_router.get(
    "/verify",
)
async def confirm_email(
        background_tasks: BackgroundTasks,
        current_user: User = Depends(get_current_user),
        redis: Redis = Depends(get_redis),
):
    key = uuid4().__str__()
    await add_key(redis, key, str(current_user.id))
    background_tasks.add_task(verify_email, current_user.email, key)
    return {"message": "Verification key sent to your email"}


@user_router.patch(
    "/change_email",
    response_model=UserSchema,
)
async def change_email(
        update_form: UserEmail = Body(),
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_session),
):
    user = await update_user_info(session, current_user, UserInfo(email=update_form.email, email_verified=False))
    if user:
        return UserSchema.from_orm(user)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Email already exists.",
    )
