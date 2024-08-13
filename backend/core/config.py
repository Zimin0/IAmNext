import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class ProjectSettings:
    PROJECT_NAME:str = "IAMNEXT"
    PROJECT_VERSION: str = "1.0.0"
    UPLOAD_PATH: str = "uploads"

    ### Database ###
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    ### JWT ###
    ACCESS_TOKEN_EXPIRE_MINUTES = 30 
    SECRET_KEY :str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"                       

project_settings = ProjectSettings()
