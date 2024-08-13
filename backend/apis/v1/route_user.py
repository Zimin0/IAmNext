from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, HTTPException

from db.session import get_db
from db.models.user import User
from schemas.user import UserCreate, UserGet
from apis.v1.dependencies import verify_active_user, verify_admin_user
from db.crud.user import create_user_db, read_user_db, delete_user_db, update_user_db

router = APIRouter()

USER_NOT_FOUND = "User not found"

@router.get('/user/me', response_model=UserGet)
async def get_my_user(db: Session = Depends(get_db), current_user: User = Depends(verify_active_user)):
    """ GET. Возвращает информацию о себе. """
    response_obj = UserGet.model_validate(current_user) # Метод model_validate служит для преобразования ORM модели в объект схемы Pydantic, выполняя валидацию данных в процессе.
    return response_obj

@router.get("/user/{nickname}", response_model=UserGet)
async def get_user(nickname:str, db: Session = Depends(get_db)):
    """ GET. Возвращает информацию о пользователе по его nickname. """
    user_in_db = read_user_db(db=db, nickname=nickname)
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=USER_NOT_FOUND)
    return user_in_db

################## ЗАМЕНЕН НА register_user эдпоинт ##################
# @router.post('/user', response_model=UserGet, status_code=status.HTTP_201_CREATED, tags=["admin only"], summary="Create a new user (Admin Only)", description="This endpoint is accessible only by admin users.",)
# def create_user(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(verify_admin_user),):
#     """ POST """
#     user_in_db = create_user_db(db=db, user=user_in_db)
#     if not user_in_db: # пользователь уже существует
#         raise HTTPException(status_code=400, detail="User already exists.")
#     return user_in_db

@router.put('/user', response_model=UserGet, status_code=status.HTTP_201_CREATED)
def update_user(user_request: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(verify_active_user)):
    """ PUT """
    user_in_db = update_user_db(db=db, user=user_request)
    if not user_in_db:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    return user_in_db

@router.delete('/user', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: Session = Depends(get_db), current_user: User = Depends(verify_active_user)):
    """ DELETE """
    user_in_db = delete_user_db(db=db, email=current_user.email)
    if not user_in_db:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    return {"detail": "User deleted."}
