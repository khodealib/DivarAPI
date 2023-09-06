import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.users import router as user_routers
from config import DOCS

__version__ = "0.1.0"

app = FastAPI(
    title="DivarAPI",
    description="Implemented Divar website api with FastAPI",
    version=__version__,
    docs_url='/docs' if DOCS else None,
    redoc_url='/redoc' if DOCS else None
)
logger = logging.getLogger('uvicorn.error')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routers, tags=['users'])
