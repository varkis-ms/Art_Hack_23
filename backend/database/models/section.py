from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from backend.database import DeclarativeBase


class Section(DeclarativeBase):
    __tablename__ = "section"

    section_id = Column(
        "section_id",
        UUID(as_uuid=True),
        unique=True,
        primary_key=True,
        doc="Unique index of element (type UUID).",
    )
    name = Column(
        "name",
        VARCHAR,
    )
    content_id = Column(
        "content_id",
        UUID(as_uuid=True),
        ForeignKey("educational_content.id"),
        doc="Unique index of element (type UUID).",
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
