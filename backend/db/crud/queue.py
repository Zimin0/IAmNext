from sqlalchemy.orm import Session
from typing import Optional

from core.hashing import Hasher
from db.models.queue import Queue 
from schemas.user import UserCreate

def __read_queue_by_id(db: Session, queue_id: int) -> Optional[Queue]:
    return db.query(Queue).filter(Queue.id == queue_id).first()

####### CREATE #######
def create_queue_db(db: Session):
    """ CREATE """
    ...

######## READ ########
def read_queue_db(db: Session, queue_id: int) -> Optional[Queue]:
    """ READ """
    queue_in_db = __read_queue_by_id(db, queue_id)
    return queue_in_db

####### UPDATE #######
####### DELETE #######