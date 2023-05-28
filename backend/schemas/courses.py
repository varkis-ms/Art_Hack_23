from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class TaskModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    level: str
    text: str
    variants: list | int | None
    correct_ans: str | int | None
    explanation: str | None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "level": "LITE",
                "text": "Кто сочиняет музыку?",
                "variants": ['дирижёр', 'композитор', 'концертмейстер', 'вокалист'],
                "correct_ans": "композитор",
                "explanation": "Композитор – автор, создатель музыкальных произведений"
            }
        }


class TaskModelUpdate(BaseModel):
    level: str
    text: str
    variants: list | int | None
    correct_ans: str | int | None
    explanation: str | None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "level": "LITE",
                "text": "Кто сочиняет музыку?",
                "variants": ['дирижёр', 'композитор', 'концертмейстер', 'вокалист'],
                "correct_ans": "композитор",
                "explanation": "Композитор – автор, создатель музыкальных произведений"
            }
        }


class VideoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    video_url: str | None
    score: int | None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

