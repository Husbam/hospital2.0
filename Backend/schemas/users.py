from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class EstatusEnum(str, Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'
    Bloqueado = 'Bloqueado'
    Suspendido = 'Suspendido'

class UserBase(BaseModel):
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: str
    Password: str
    Numero_Telefonico_Movil: str
    Estatus: EstatusEnum
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    Persona_ID: Optional[int] = None
    Nombre_Usuario: Optional[str] = None
    Correo_Electronico: Optional[str] = None
    Password: Optional[str] = None
    Numero_Telefonico_Movil: Optional[str] = None
    Estatus: Optional[EstatusEnum] = None
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

class User(UserBase):
    ID: int
    class Config:
        from_attributes = True
