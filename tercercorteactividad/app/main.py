from fastapi import FastAPI
from app import models, crud, database
from sqlalchemy.orm import Session

app = FastAPI()

# Crea las tablas
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"message": "Sistema Solar API"}

@app.post("/sistemas/")
def crear_sistema(nombre: str, cantidad_planetas: int, db: Session = database.get_db()):
    return crud.crear_sistema(db, nombre, cantidad_planetas)

@app.post("/planetas/")
def crear_planeta(nombre: str, tamaño: str, distancia_sol: float, sistema_id: int, db: Session = database.get_db()):
    return crud.crear_planeta(db, nombre, tamaño, distancia_sol, sistema_id)

@app.get("/planetas/")
def listar_planetas(db: Session = database.get_db()):
    return crud.listar_planetas(db)
