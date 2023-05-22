from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.database import DeclarativeBase


class AccessToMaterial(DeclarativeBase):
    __tablename__ = "access_to_material"

    id = Column(
        "id",
        UUID(as_uuid=True),
        server_default=func.gen_random_uuid(),
        primary_key=True,
        doc="Unique index of element (type UUID).",
    )
    user_id = Column(
        "user_id",
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        doc="Unique index of element (type UUID).",
    )
    section_id = Column(
        "section_id",
        UUID(as_uuid=True),
        ForeignKey("section.section_id"),
        doc="Unique index of element (type UUID).",
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
