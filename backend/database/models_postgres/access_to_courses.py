from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, VARCHAR, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from backend.database import DeclarativeBase


class AccessToCourses(DeclarativeBase):
    __tablename__ = "access_to_courses"

    id = Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
        doc="Unique index of element (type UUID).",
    )
    user_id = Column(
        "user_id",
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        doc="Unique index of element (type UUID).",
    )
    course_id = Column(
        "course_id",
        UUID(as_uuid=True),
        ForeignKey("courses.course_id"),
        doc="Unique index of element (type UUID).",
    )
    dt_created = Column(
        "dt_created",
        TIMESTAMP,
        server_default=func.current_timestamp(),
    )

    course_name = relationship(
        "Courses", uselist=False, backref="access_to_courses", lazy=False
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
