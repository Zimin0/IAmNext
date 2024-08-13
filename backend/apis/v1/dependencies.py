from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from core.config import project_settings
from db.session import get_db
from db.models.user import User
from db.crud.user import read_user_db
from core.hashing import Hasher

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def _get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """ Возвращает пользователя по токену. """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверные данные для входа.",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, project_settings.SECRET_KEY, algorithms=[project_settings.ALGORITHM])
        nickname = payload.get('sub')
        if nickname is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = read_user_db(db=db, nickname=nickname)
    if user is None:
        raise credentials_exception
    return user

def verify_active_user(current_user: User = Depends(_get_current_user)) -> User:
    """Проверяет, активен ли пользователь. """
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
    return current_user

def verify_admin_user(current_user: User = Depends(_get_current_user)) -> User:
    """ Проверяет, является ли пользователь admin'ом. """
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="The user doesn't have enough privileges")
    return current_user


