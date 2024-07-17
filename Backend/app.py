from fastapi import FastAPI
<<<<<<< HEAD
from routes.users import user
from routes.persons import person
from routes.rol import rol
from routes.usersrol import userrol
=======
from routes.user import user
from routes.persons import person
from routes.rol import rol
from routes.userrol import userrol
from routes.persona import persona
from routes.usuarios import usuarios

app=FastAPI()
#app.include_router(persona,prefix="/api/personas",tags=["Personas"])
#app.include_router(usuarios,prefix="/api/usuarios",tags=["usuarios"])
>>>>>>> ddc1853e4c2e93d1ae48019a4ec36955f014376a

app=FastAPI(
    title="Hospital",
    description="API para el almacenamiento de informacipn de un hospital"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
<<<<<<< HEAD
print ("Hola bienvenido a mi backend")
=======
print("Bienvenido a mi aplicacion")
>>>>>>> ddc1853e4c2e93d1ae48019a4ec36955f014376a
