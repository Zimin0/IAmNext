from sqlalchemy.orm import Session
from typing import Optional

from core.hashing import Hasher
from db.models.queue import Queue 
from schemas.user import UserCreate
from schemas.queue import QueueCreate

def __read_queue_by_id(db: Session, queue_id: int) -> Optional[Queue]: # не инт, а стринг
    return db.query(Queue).filter(Queue.id == queue_id).first()

####### CREATE #######
def create_queue_db(db: Session, queue: QueueCreate) -> Optional[Queue]:
    """ CREATE """
    queue_in_db = __read_queue_by_id(db, queue.id)
    if queue_in_db:
        return None
    
    queue_obj = Queue(
        name=queue.name,
        discriptio=queue.discription,
        max_amount_people=queue.max_amount_people,
        owner_id=queue.owner_id,    
    )

    db.add(queue_obj)
    db.commit()
    db.refresh(queue)
    return queue_obj

######## READ ########
def read_queue_db(db: Session, queue_id: int) -> Optional[Queue]:
    """ READ """
    queue_in_db = __read_queue_by_id(db, queue_id)
    return queue_in_db

####### UPDATE #######
####### DELETE #######