from datetime import date, datetime

from pydantic import BaseModel, EmailStr, constr


class UserSchema(BaseModel):
    login: str | None
    email: EmailStr | None
    birthday: date | None
    score: int | None
    displayed_name: str | None
    full_name: str | None
    # dt_created: datetime
    # dt_updated: datetime

    class Config:
        orm_mode = True


class UserRequest(BaseModel):
    # TODO: функция бизнес-логики для валидации логина и имени
    login: str | None
    birthday: date | None
    displayed_name: str | None
    full_name: str | None
    # dt_created: datetime
    # dt_updated: datetime


class UserInfo(BaseModel):
    login: str | None = None
    email: EmailStr | None = None
    email_verified: bool | None = None
    score: int | None = None
    birthday: date | None = None
    displayed_name: str | None = None
    full_name: str | None = None
    # password: str | None


class UserEmail(BaseModel):
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "email": "anth@mail.com",
            }
        }


class UserFriends(BaseModel):
    user_id: str
    friend_id: str
    related_type: str

    class Config:
        schema_extra = {
            "example": {
                "email": "anth@mail.com",
            }
        }


class UserScoreRequest(BaseModel):
    score: int


class UserScoreResponse(BaseModel):
    score: int

    class Config:
        orm_mode = True
