from .Timestamps import TimestampedModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum
import enum

class SocialMediaStatus(enum.Enum):
    active = 'active'
    pending = 'pending'
    deactive = 'deactive'

class SocialMedia(TimestampedModel):
    __tablename__ = 'social_media'

    id: Mapped[int] = mapped_column(primary_key=True)
    media_domain_name: Mapped[str] = mapped_column(nullable=False)
    profile_linK: Mapped[str] = mapped_column(nullable=False) 
    # status: Mapped[str] = mapped_column(
    #     Enum(SocialMediaStatus),
    #     default=SocialMediaStatus.pending.value,
    #     nullable = False,
    # )
