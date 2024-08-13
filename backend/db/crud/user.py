from sqlalchemy.orm import Session
from typing import Optional

from core.hashing import Hasher
from db.models.user import User 
from schemas.user import UserCreate


def __read_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

def __read_user_by_nickname(db: Session, nickname: str) -> Optional[User]:
    return db.query(User).filter(User.nickname == nickname).first()

####### CREATE #######
def create_user_db(db: Session, user: UserCreate) -> Optional[User]:
    """ CREATE """
    user_in_db = __read_user_by_nickname(db, user.nickname)
    if user_in_db:
        return None
    
    user_obj = User(
        nickname=user.nickname,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_admin=False
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

####### READ #######
def read_user_db(db: Session, nickname: str) -> Optional[User]:
    """ READ """
    user_in_db = __read_user_by_nickname(db, nickname)
    return user_in_db

####### UPDATE #######
def update_user_db(db: Session, user: UserCreate) -> Optional[User]:
    """ UPDATE """
    user_in_db = __read_user_by_nickname(db, user.nickname)
    if not user_in_db:
        return None
    user_in_db.nickname = user.nickname
    user_in_db.password = Hasher.get_password_hash(user.password)
    db.commit()
    db.refresh(user_in_db)
    return user_in_db

####### DELETE #######
def delete_user_db(db: Session, nickname) -> bool:
    """ DELETE """
    user_in_db = __read_user_by_nickname(db, nickname)
    if user_in_db:
        return False
    db.delete(user_in_db)
    db.commit()
    return True
