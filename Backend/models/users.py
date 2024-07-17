from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
<<<<<<< HEAD
import models.persons
import enum

class MyEstatus(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"
    

class User(Base):
    __tablename__ = "tbb_usuarios"

    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))
=======
from enum import Enum


# Definición de los valores del Enum
class EstatusEnum(str, Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'
    Bloqueado = 'Bloqueado'
    Suspendido = 'Suspendido'

class User(Base):
    __tablename__ = "tbb_usuarios"
    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))#
>>>>>>> ddc1853e4c2e93d1ae48019a4ec36955f014376a
    Nombre_Usuario = Column(String(60))
    Correo_Electronico = Column(String(100))
    Contrasena = Column(String(40))
    Numero_Telefonico_Movil = Column(String(20))
<<<<<<< HEAD
    Estatus = Column(Enum(MyEstatus))
=======
    Estatus = Column(SQLAlchemyEnum(EstatusEnum), nullable=False)
>>>>>>> ddc1853e4c2e93d1ae48019a4ec36955f014376a
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    # Clave foránea para la relación uno a uno con User
    
