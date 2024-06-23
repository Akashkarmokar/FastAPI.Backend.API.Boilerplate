from .Timestamps import TimestampedModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text


class Bio(TimestampedModel):
    __tablename__ = 'bios'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Text] = mapped_column(Text,nullable=True)
    note: Mapped[Text] = mapped_column(Text,nullable=True)
    designation: Mapped[Text] = mapped_column(Text, nullable=True)
    image_key: Mapped[Text] = mapped_column(Text, nullable=True) 

    
    
    
