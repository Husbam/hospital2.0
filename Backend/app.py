from fastapi import FastAPI
from routes.users import user
from routes.personas import person
from routes.persona import persona
from routes.usuarios import usuarios

app=FastAPI()
#app.include_router(persona,prefix="/api/personas",tags=["Personas"])
#app.include_router(usuarios,prefix="/api/usuarios",tags=["usuarios"])

app.include_router(user)
app.include_router(person)
print("Bienvenido a mi aplicacion")