from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class SistemaSolar(Base):
    __tablename__ = "sistemas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    cantidad_planetas = Column(Integer)

    planetas = relationship("Planeta", back_populates="sistema")

class Planeta(Base):
    __tablename__ = "planetas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tamaño = Column(String)
    distancia_sol = Column(Float)
    sistema_id = Column(Integer, ForeignKey("sistemas.id"))

    sistema = relationship("SistemaSolar", back_populates="planetas")
