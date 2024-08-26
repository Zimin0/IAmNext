from db.base_class import Base
from sqlalchemy.orm import relationship
from db.utils import generate_numeric_uuid
from sqlalchemy import Integer, Column, String, String, ForeignKey, DateTime

class UserInQueue(Base):
    __tablename__ = 'user_in_queue'
    id = Column(String(22), index=True, unique=True, default=generate_numeric_uuid)    
    user_id = Column(String, ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    queue_id = Column(String, ForeignKey("queues.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    position = Column(Integer, nullable=False, default=1)

    user = relationship("User", back_populates="queues")
    queue = relationship("Queue", back_populates="users")
    quue = relationship("Queue", back_populates="queues") 
    