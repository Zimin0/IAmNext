from db.utils import generate_numeric_uuid
from db.base_class import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, String, Integer

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, index=True, unique=True, primary_key=True, default=generate_numeric_uuid)
    nickname = Column(String, unique=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    queues = relationship("UserInQueue", back_populates="user", cascade="all, delete-orphan")