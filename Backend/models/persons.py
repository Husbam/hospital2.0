from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Titulo = Column(String(20))
    Nombre = Column(String(80), nullable=False)
    Primer_Apellido = Column(String(80), nullable=False)
    Segundo_Apellido = Column(String(80))
    CURP = Column(String(18), unique=True)
    Genero = Column(Enum('M', 'F', 'N/B', name='genero_enum'), nullable=False)
    Grupo_Sanguineo = Column(Enum('A+','A-', 'B+','B-', 'AB+','AB-', 'O+','O-', name='grupo_sanguineo_enum'), nullable=False)
    Fecha_Nacimiento = Column(DateTime, nullable=False)
    Estatus = Column(Boolean, nullable=False, default=True)
    Fecha_Registro = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime)
    #items = relationship("Item", back_populates="owner")