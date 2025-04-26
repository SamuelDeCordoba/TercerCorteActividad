from app import models
from sqlalchemy.orm import Session

def crear_sistema(db: Session, nombre: str, cantidad_planetas: int):
    sistema = models.SistemaSolar(nombre=nombre, cantidad_planetas=cantidad_planetas)
    db.add(sistema)
    db.commit()
    db.refresh(sistema)
    return sistema

def crear_planeta(db: Session, nombre: str, tamaño: str, distancia_sol: float, sistema_id: int):
    planeta = models.Planeta(nombre=nombre, tamaño=tamaño, distancia_sol=distancia_sol, sistema_id=sistema_id)
    db.add(planeta)
    db.commit()
    db.refresh(planeta)
    return planeta

def listar_planetas(db: Session):
    return db.query(models.Planeta).all()
