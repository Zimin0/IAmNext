from core.hashing import Hasher
from sqlalchemy.orm import Session
from db.crud.user import read_user_db

def authenticate_user(nickname: str, password: str, db: Session):
    """ Authenticate user by nickname and password. """
    user = read_user_db(nickname=nickname, db=db)
    if not user: # Пользователь не найден
        return False
    if not Hasher.verify_password(password, user.password): # Неверный пароль
        return False
    return user