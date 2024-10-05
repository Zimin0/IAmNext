from pydantic import BaseModel, Field
from typing import Optional

class QueueGet(BaseModel):
    """Get a queue from database."""
    id: int
    name: str
    discription: str
    max_amount_people: int
    owner_id: int

    class Config():
        orm_mode = True
        from_attribute = True

class QueueCreate(BaseModel):
    """Create a new queue in database."""
    name: str = Field(..., min_length=8, max_length=60)
    discription: str = Field(default="No description.")
    max_amount_people: int = Field(default=1, ge=0, lt=100) # ??????
    owner_id: int
