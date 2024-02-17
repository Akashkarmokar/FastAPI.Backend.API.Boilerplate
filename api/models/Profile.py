from datetime import datetime
from .Timestamps import TimestampedModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text

class Profile(TimestampedModel):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    organization_name: Mapped[str] = mapped_column(nullable=False)
    designation: Mapped[str] = mapped_column(nullable=False)
    joining_date: Mapped[datetime] = mapped_column(nullable=False)
    last_working_date: Mapped[datetime] = mapped_column(nullable=True)
    notes: Mapped[Text] = mapped_column(Text, nullable= True)
    
