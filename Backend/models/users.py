from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
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
    Persona_ID = Column(Integer)#
    Nombre_Usuario = Column(String(60))
    Correo_Electronico = Column(String(100))
    Password = Column(LONGTEXT)
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column(SQLAlchemyEnum(EstatusEnum), nullable=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    # items = relationship("Item", back_populates="owner")  # Clave Foranea
