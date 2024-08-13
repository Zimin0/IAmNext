from jose import jwt
from typing import Optional
from datetime import datetime, timedelta, timezone

from core.config import project_settings

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Creates an access token using the JSON Web Tokens (JWT) library.
    """
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=project_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, project_settings.SECRET_KEY, algorithm=project_settings.ALGORITHM)
