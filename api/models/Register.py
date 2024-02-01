from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from .Timestamps import TimestampedModel
from sqlalchemy.orm import Relationship
from api.core.db import AsyncSession
from enum import Enum


class UserStatus(Enum):
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    DISABLE = "DISABLE"


class Register(TimestampedModel):
    __tablename__ = 'registers'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[UserStatus]