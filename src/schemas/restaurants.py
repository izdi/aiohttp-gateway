from datetime import datetime

from pydantic import BaseModel

__all__ = (
    'CreateRestaurant',
    'UpdateRestaurant',
)


class CreateRestaurant(BaseModel):
    name: str
    opens_at: datetime
    closes_at: datetime


class UpdateRestaurant(BaseModel):
    name: str = None
    opens_at: datetime = None
    closes_at: datetime = None
