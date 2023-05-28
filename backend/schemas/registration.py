from pydantic import BaseModel, EmailStr, Field, root_validator, validator

from backend.config import get_settings


class RegistrationForm(BaseModel):
    email: EmailStr
    password1: str
    password2: str

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get("password1"), values.get("password2")
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError("Passwords do not match")
        return values


class VkTokenAuth(BaseModel):
    vk_id: int


class RegistrationFormInDb(BaseModel):
    email: EmailStr
    password: str = Field(alias="password1")

    @validator("password")
    def validate_password(cls, password):
        password = get_settings().PWD_CONTEXT.hash(password)
        return password


class RegistrationResponse(BaseModel):
    message: str
