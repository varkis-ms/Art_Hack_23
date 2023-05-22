from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import BOOLEAN, UUID, VARCHAR
from sqlalchemy.sql import func

from backend.database import DeclarativeBase


class EducationalContent(DeclarativeBase):
    __tablename__ = "educational_content"

    id = Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
        doc="Unique index of element (type UUID).",
    )
    related_topics = Column(
        "related_topics",
        UUID(as_uuid=True),
        ForeignKey("topics.id"),
        doc="Unique index of element (type UUID).",
    )
    name = Column(
        "name",
        VARCHAR,
        nullable=False,
    )
    content = Column(
        "content",
        VARCHAR,
    )
    private = Column(
        "private",
        BOOLEAN,
        nullable=False,
        default=True,
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
