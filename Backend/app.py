from fastapi import FastAPI
from routes.persona import persona
from routes.usuarios import usuarios

app=FastAPI()
app.include_router(persona,prefix="/api/personas",tags=["Personas"])
app.include_router(usuarios,prefix="/api/usuarios",tags=["usuarios"])

print("Bienvenido a mi aplicacion")