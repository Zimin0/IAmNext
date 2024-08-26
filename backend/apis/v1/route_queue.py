from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, HTTPException

from db.session import get_db
from db.models.user import User
from schemas.user import UserCreate, UserGet
from apis.v1.dependencies import verify_active_user, verify_admin_user
from db.crud.user import create_user_db, read_user_db, delete_user_db, update_user_db


router = APIRouter()


async def get_queue(db: Session = Depends(get_db)):
    """GET. Возвращает информацию об очереди."""
    response_obj = ...