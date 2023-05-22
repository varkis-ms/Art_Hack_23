from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.database import DeclarativeBase


class Interests(DeclarativeBase):
    __tablename__ = "interests"

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
    topic_id = Column(
        "topic_id",
        UUID(as_uuid=True),
        ForeignKey("topics.id"),
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
