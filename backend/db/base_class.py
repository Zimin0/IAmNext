from typing import Any
from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative

@as_declarative()
class Base:
    id: Any
    __name__: str
