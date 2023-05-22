from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from backend.database import DeclarativeBase


class Topics(DeclarativeBase):
    __tablename__ = "topics"

    id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        primary_key=True,
        doc="Unique index of element (type UUID).",
    )
    name = Column(
        "name",
        VARCHAR,
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
