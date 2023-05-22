from fastapi import APIRouter, Body, Depends, Form, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from backend.config import get_settings
from backend.database.models import User
from backend.schemas import (
    RegistrationForm,
    RegistrationFormInDb,
    RegistrationResponse,
    Token,
    UserSchema,
)
from backend.utils.user.auth_db import *
from backend.utils.user.business_logic import *

auth_router = APIRouter(tags=["auth"], prefix="/user")


@auth_router.post(
    "/auth",
    response_model=Token,
)
async def auth(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session),
):
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=get_settings().ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get(
    "/me",
    response_model=UserSchema,
)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return UserSchema.from_orm(current_user)


@auth_router.post(
    "/registration",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Bad parameters for registration",
        },
    },
)
async def registration(
    registration_form: RegistrationForm = Body(),
    session: AsyncSession = Depends(get_session),
):
    user_data = RegistrationFormInDb(**registration_form.dict())
    check_user = await register_user(session, user_data)
    if check_user:
        return RegistrationResponse(message="Successful registration!")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Email already exists.",
    )
