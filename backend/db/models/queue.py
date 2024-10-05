from db.utils import generate_numeric_uuid
from db.base_class import Base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Queue(Base):
    __tablename__ = 'queues'
    id = Column(String(22), index=True, primary_key=True, unique=True, default=generate_numeric_uuid)
    name = Column(String, index=True)  # минимальная длина в 5 символов
    discription = Column(String, nullable=True)
    max_amount_people = Column(Integer, default=1)
    owner_id = Column(Integer, ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)

    # Связь с пользователем (владельцем очереди)
    owner = relationship("User", back_populates="owned_queues")

    # Связь с UserInQueue (пользователи в очереди)
    users = relationship("UserInQueue", back_populates="queue", cascade="all, delete-orphan")
