from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.sql import func

from backend.database import DeclarativeBase
from backend.database.enums.friend import Relation_type


class Friends(DeclarativeBase):
    __tablename__ = "friends"

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
    friend_id = Column(
        "friend_id",
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        doc="Unique index of element (type UUID).",
    )
    relation_type = Column(
        "relation_type",
        VARCHAR,
        nullable=False,
        default=Relation_type.not_approved_friend.value,
    )

    def __repr__(self):
        columns = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
