from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import relationship

from backend.database import DeclarativeBase


class AuthTablePassword(DeclarativeBase):
    __tablename__ = "auth_table_password"

    id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        onupdate="CASCADE",
        primary_key=True,
        doc="Unique index of element (type UUID).",
    )
    password = Column(
        "password",
        VARCHAR,
        nullable=False,
        doc="Hashed password.",
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
