from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import BOOLEAN, DATE, UUID, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import DeclarativeBase
from backend.database.enums.role import Role


class User(DeclarativeBase):
    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
        unique=True,
        doc="Unique index of element (type UUID).",
    )
    login = Column(
        "login",
        VARCHAR,
        nullable=True,
        unique=True,
        index=True,
        doc="Login for authentication.",
    )
    email = Column(
        "email",
        VARCHAR,
        nullable=False,
        unique=True,
        index=True,
        doc="Email for authentication and notifications.",
    )
    full_name = Column(
        "full_name",
        VARCHAR,
        nullable=True,
    )
    displayed_name = Column(
        "displayed_name",
        VARCHAR,
        nullable=True,
    )
    birthday = Column(
        "birthday",
        DATE,
        nullable=True,
    )
    role = Column("role", VARCHAR, nullable=False, default=Role.user.value)
    allowed_to_create = Column(
        "allowed_to_create",
        BOOLEAN,
        nullable=False,
        default=False,
    )

    password = relationship(
        "AuthTablePassword", uselist=False, backref="user", lazy=False
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
