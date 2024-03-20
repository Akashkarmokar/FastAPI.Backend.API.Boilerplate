from pydantic import BaseModel
from enum import Enum


class ActionType(str, Enum):
    get_url = 'get_url'
    save_key = 'save_key'
    others = 'regular'


class ProfileChange(BaseModel):
    action: ActionType
    name:str = None
    note: str = None
    image_key: str = None
    designation: str = None

