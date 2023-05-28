from fastapi import APIRouter, Body, Depends, Form, status, HTTPException, Query, Request
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy.ext.asyncio import AsyncSession

from backend.utils.user.business_logic import get_current_user, get_session
from backend.database.connection import get_mongo
from backend.schemas import TaskModel, UserInfo, UserScoreResponse, UserScoreRequest
from backend.utils.user.auth_db import *
from backend.utils.user import update_user_info
from backend.utils.task import get_list, get_task_from_id
from backend.database.enums import Role

task_router = APIRouter(tags=["task"], prefix="/test")


@task_router.get(
    "/",
    response_model=TaskModel,
)
async def get_task(
        task_id: str = Query(),
        current_user: User = Depends(get_current_user),
        mongo_session: AsyncIOMotorClient = Depends(get_mongo),
):
    task = await get_task_from_id(mongo_session, task_id)
    if task:
        return task
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unknown task_id")


@task_router.post(
    "/score",
    response_model=UserScoreResponse,
)
async def add_score(
        user_score: UserScoreRequest = Body(),
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_session),
):
    user = await update_user_info(session, current_user, UserInfo(score=current_user.score + user_score.score))
    if user:
        return UserScoreResponse.from_orm(user)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Unknown error.",
    )


@task_router.post(
    "/",
    response_model=TaskModel,
)
async def add_task(
        task_info: TaskModel,
        # current_user: User = Depends(get_current_user),
        mongo_session: AsyncIOMotorClient = Depends(get_mongo),
):
    # if current_user.role == Role.user:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="You do not have permission to perform this action")
    mongo_db = mongo_session.art_db
    new_task = await mongo_db[f"topic_{topic_id}"].insert_one(jsonable_encoder(task_info))
    created_task = await mongo_db[f"topic_{topic_id}"].find_one({"_id": new_task.inserted_id})
    return created_task


@task_router.get(
    "/list",
)
async def get_list_test(
        current_user: User = Depends(get_current_user),
        mongo_session: AsyncIOMotorClient = Depends(get_mongo),
):
    return await get_list(mongo_session)
