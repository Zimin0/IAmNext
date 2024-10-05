from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from core.security import create_access_token
from schemas.token import Token
from schemas.user import UserCreate
from db.session import get_db
from db.crud.user import create_user_db, read_user_db
from db.models.user import User
from apis.v1.utils import authenticate_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_in_db = create_user_db(db=db, user=user)
    ...
    # Дополнительный функционал - например - подтверждение почты.
    ...
    if not user_in_db:
        raise HTTPException(status_code=400, detail="User already exists.")
    return user_in_db

@router.post("/login", response_model=Token, summary="Login and get an access token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.nickname})
    return {"access_token": access_token, "token_type": "bearer"}

async def delete_account():
    ... # идея в том, чтобы аккант отключался на месяц и мог быть восстановлен.
