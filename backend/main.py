from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from core import config
from db.session import engine
from db.base_class import Base
from apis.base import api_router

def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app:FastAPI, api_router):
    app.include_router(api_router)

def start_applications(lifespan=None):
    app = FastAPI(
        title=config.project_settings.PROJECT_NAME,
        version=config.project_settings.PROJECT_VERSION,
        lifespan=lifespan
    )
    create_tables()
    include_router(app, api_router)
    return app

app = start_applications()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def check_website():
    html_content = "<h2>Website is up.</h2>"
    return HTMLResponse(content=html_content)