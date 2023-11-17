from fastapi import FastAPI 
#Importamos de la carpeta: "routers" el código o las clases: "routers_5" y "routers2_5"
from routers import router1, router2, router3,  router5, router6, router7, router8, router9, router_DB_10, router_DB_11

from fastapi.staticfiles import StaticFiles


#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

#Creamos un router a partir de la clase router1
app.include_router(router1.router)
#Creamos un router a partir de la clase router2
app.include_router(router2.router)
#Creamos un router a partir de la clase router3
app.include_router(router3.router)
#Creamos un router a partir de la clase router4

#Creamos un router a partir de la clase router5
app.include_router(router5.router)
#Creamos un router a partir de la clase router6
app.include_router(router6.router)
#Creamos un router a partir de la clase router7
app.include_router(router7.router)
#Creamos un router a partir de la clase router8
app.include_router(router8.router)
#Creamos un router a partir de la clase router9
app.include_router(router9.router)



#Creamos un router a partir de la clase router_DB_10
app.include_router(router_DB_10.router)
app.include_router(router_DB_11.router)

#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/")

#creamos la función asincrona "imprimir"
async def imprimir():
    return "Hola estudiantes"


#Levantamos el server Uvicorn
#-uvicorn main:app --reload-
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000

#########################################Segunda Parte################################################

#creamos la función asincrona con formato JSON
@app.get("/Git")
async def imprimir():
    return {"Git_curso":"https://github.com/freddy-7777/Modelos-de-desarrollo-WEB.git"}

# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/Git

######################################CLASE 3################################

#Detener server con: ctrl + c


#Documentación con Swagger:  http://127.0.0.1:8000/docs
#Documentación con Redocly:  http://127.0.0.1:8000/redoc