from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

persona = APIRouter()
personas=[]

class model_personas(BaseModel):
    id:int
    nombre:str
    primer_apellido:str
    segundo_apellido:Optional[str]
    edad:int
    fecha_nacimiento: datetime
    curp: str
    tipo_sangre: str
    created_at: datetime = datetime.now()
    estatus: bool = False

# Obtener todas las personas
@persona.get('/personas')
def getPersonas():
    return personas

# Obtener una persona por su ID
@persona.get('/personas/{persona_id}')
def getPersona(persona_id: int):
    for persona in personas:
        if persona['id'] == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Guardar una nueva persona
@persona.post('/personas')
def save_persona(datos_persona: model_personas):
    personas.append(datos_persona.dict())
    return "Datos guardados correctamente"

# Actualizar datos de una persona por su ID
@persona.put('/personas/{persona_id}')
def updatePersona(persona_id: int, datos_persona: model_personas):
    for index, persona in enumerate(personas):
        if persona['id'] == persona_id:
            personas[index] = datos_persona.dict()
            return "Datos actualizados correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Eliminar una persona por su ID
@persona.delete('/personas/{persona_id}')
def deletePersona(persona_id: int):
    for index, persona in enumerate(personas):
        if persona['id'] == persona_id:
            del personas[index]
            return "Persona eliminada correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")
