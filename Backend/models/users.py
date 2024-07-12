from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

# Definición de los valores del Enum
estatus_enum = Enum('Activo', 'Inactivo', 'Bloqueado', 'Suspendido', name="estatus_enum")

class User(Base):
    __tablename__ = "users"
    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer)
    Nombre_Usuario = Column(String(60))
    Correo_Electronico = Column(String(100))
    Password = Column(LONGTEXT)
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column(estatus_enum)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    # items = relationship("Item", back_populates="owner")  # Clave Foranea
