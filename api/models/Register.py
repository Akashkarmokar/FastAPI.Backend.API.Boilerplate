from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum
from .Timestamps import TimestampedModel
import enum
# from sqlalchemy.dialects.postgresql import ENUM as pgEnum

class Status(enum.Enum):
    active = 'active'
    pending = 'pending'
    deactive = 'deactive'


class Register(TimestampedModel):
    __tablename__ = 'registers'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    # alive_status = mapped_column(
    #     Enum(Status),
    #     default=Status.pending.value,
    #     nullable=False,
    #     server_default=Status.pending.value
    # )