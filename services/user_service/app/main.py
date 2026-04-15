from fastapi import FastAPI
from .routes import router
from .db import engine, Base

app = FastAPI(
    title="User Service"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)
