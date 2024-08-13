## Create database
1) Go to PGadmin
2) Create new db with name from .env
3) alembic init alembic
4) Add code too env.py [1]
5) alembic revision --autogenerate -m "first commit"
6) uvicorn main:app --reload

[1]
"""
config = context.config

#new
config.set_main_option("sqlalchemy.url",settings.DATABASE_URL)

target_metadata = Base.metadata 
"""

[2]
https://www.fastapitutorial.com/blog/alembic-database-fastapi/