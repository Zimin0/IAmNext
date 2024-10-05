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

    # Связь с очередями, которыми пользователь владеет
    owned_queues = relationship("Queue", back_populates="owner")

    # Связь с таблицей UserInQueue (участие пользователя в очередях)
    queues = relationship("UserInQueue", back_populates="user", cascade="all, delete-orphan")


from db.utils import generate_numeric_uuid
from db.base_class import Base
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class UserInQueue(Base):
    __tablename__ = 'user_in_queue'
    id = Column(String(22), primary_key=True, index=True, unique=True, default=generate_numeric_uuid)
    user_id = Column(Integer, ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    queue_id = Column(String, ForeignKey("queues.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    position = Column(Integer, nullable=False, default=1)

    # Связь с таблицей User (пользователь в очереди)
    user = relationship("User", back_populates="queues")

    # Связь с таблицей Queue (очередь, в которой находится пользователь)
    queue = relationship("Queue", back_populates="users")
