from pydantic import BaseModel
from datetime import date


class AddMediaDTO(BaseModel):
    organization_name: str
    designation: str
    joining_date: date
    last_working_date: date = None
    notes: str = None