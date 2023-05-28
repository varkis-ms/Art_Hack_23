from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.sql import func

from backend.database import DeclarativeBase


class Courses(DeclarativeBase):
    __tablename__ = "courses"

    course_id = Column(
        "course_id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
        doc="Unique index of element (type UUID).",
    )
    mongo_name = Column(
        "mongo_name",
        VARCHAR,
        nullable=False,
        unique=True,
    )
    name = Column(
        "name",
        VARCHAR,
        nullable=False,
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
