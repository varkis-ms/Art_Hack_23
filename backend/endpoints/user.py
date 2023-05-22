from fastapi import APIRouter, Body, Depends, status

from backend.database.models import User
from backend.schemas import UserRequest, UserSchema
from backend.utils.user.business_logic import (
    AsyncSession,
    get_current_user,
    get_session,
)
from backend.utils.user.user_db import update_user_info

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
    user = await update_user_info(session, current_user, update_form)
    if user:
        return UserSchema.from_orm(user)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Login already exists.",
    )
