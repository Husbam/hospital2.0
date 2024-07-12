from typing import List, Union, Literal
from pydantic import BaseModel
from datetime import datetime

# Definición de los valores del Enum
EstatusEnum = Literal['Activo', 'Inactivo', 'Bloqueado', 'Suspendido']

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

class UserUpdate(UserBase):
    pass

class User(UserBase):
    ID: int
    #owner_id: int  # Clave Foranea
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    usuario: str
    password: str


# class UserLogin(BaseModel):
#     usuario: str
#     password: str