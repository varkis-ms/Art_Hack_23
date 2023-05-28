from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.encoders import jsonable_encoder

from backend.schemas import TaskModel


async def get_list(mongo_session: AsyncIOMotorClient) -> list:
    mongo_db = mongo_session.tasks.get_collection("tasks")
    all_tasks = []
    async for task in mongo_db.find():
        all_tasks.append(task)
    return all_tasks


async def get_task_from_id(mongo_session: AsyncIOMotorClient, task_id: str) -> list:
    mongo_db = mongo_session.tasks
    return await mongo_db.tasks.find_one({"_id": task_id})
