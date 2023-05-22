from datetime import date, datetime

from pydantic import BaseModel, EmailStr, constr


class UserSchema(BaseModel):
    login: str | None
    email: EmailStr
    birthday: date | None
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
