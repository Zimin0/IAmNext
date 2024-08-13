from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserGet(BaseModel):
    """Get a user from database."""
    id: int
    nickname: str
    is_active: bool
    is_admin: bool

    class Config():
        orm_mode = True
        from_attributes = True

class UserCreate(BaseModel):
    """Create a new user."""    
    nickname: str = Field(..., min_length=4, max_length=12)
    password: str = Field(..., min_length=8, max_length=32)
