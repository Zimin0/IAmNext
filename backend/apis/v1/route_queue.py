from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, HTTPException

from db.session import get_db
from db.models.user import User
from schemas.queue import QueueCreate, QueueGet
from apis.v1.dependencies import verify_active_user, verify_admin_user
from db.crud.queue import create_queue_db, read_queue_db

router = APIRouter()

@router.get('/queue/{queue_id}', response_model=QueueGet)
async def get_queue(queue_id: str, db: Session = Depends(get_db)):
    """GET. Возвращает информацию об очереди."""
    response_obj = read_queue_db(db, queue_id)
    return response_obj

@router.post("/queue", response_model=QueueGet, status_code=status.HTTP_201_CREATED)
async def create_queue(queue_request: QueueCreate, db: Session = Depends(get_db), current_user: User = Depends(verify_admin_user)):
    """ POST. Создает новую очередь."""
    queue_in_db = create_queue_db(db, queue=queue_request)
    if not queue_in_db: # очередь уже существует
        raise HTTPException(status_code=400, detail="Queue already exists")
    return queue_in_db
