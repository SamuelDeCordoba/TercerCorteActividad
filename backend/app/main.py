from fastapi import FastAPI
from . import models
from .database import engine
from .routers import planeta, constelacion

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(planeta.router, prefix="/api")
app.include_router(constelacion.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API Planetario online!"}