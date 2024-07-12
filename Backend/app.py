from fastapi import FastAPI
from routes.user import user
from routes.persons import person
from routes.rol import rol
from routes.userrol import userrol
from routes.persona import persona
from routes.usuarios import usuarios

app=FastAPI()
#app.include_router(persona,prefix="/api/personas",tags=["Personas"])
#app.include_router(usuarios,prefix="/api/usuarios",tags=["usuarios"])

app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
print("Bienvenido a mi aplicacion")