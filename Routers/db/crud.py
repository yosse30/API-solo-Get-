#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, Depends, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

from fastapi.staticfiles import StaticFiles


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#Importamos librería jwt
from jose import jwt, JWTError
#Importamos libreria passlib (algoritmo de encriptación)
from passlib.context import CryptContext
#Importamos libreria de fechas para la expiración del token
from datetime import datetime, timedelta
#Genera respuestas HTML personalizadas
from fastapi.responses import HTMLResponse
#importamos mongo
import pymongo 


#Implementamos algoritmo de haseo para encriptar contraseña
ALGORITHM = "HS256"
#Duración de autenticación 
ACCESS_TOKEN_DURATION= 2
#Creamos un secret
SECRET="123456789"

#Creamos un objeto o instancia a partir de la clase FastAPI
app= FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

#Autenticación por contraseña para eso:
#Creamos un endpoint llamado "login"
oauth2=OAuth2PasswordBearer(tokenUrl="login")

#Creamos contexto de encriptación para eso importamos libreria passlib y elegimos algoritmo de incriptación "bcrypt"
#Utilizamos bcrypt generator para encriptar nuestras contraseñas
crypt= CryptContext(schemes="bcrypt")

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS="actividad9"
MONGO_COLECCION="alumnos"

try:
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION] 
    for documento in coleccion.find():
         print(documento)
    cliente.server_info()
    print("Conexion a mongo exitosa")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
   print("Fallo al conectarse a mongodb"+errorConexion)


class User(BaseModel):
    username:str
    full_name: str
    email:str
    disabled:bool
    phone:str


@app.get("//", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de alumnos exitosamente")
async def peliculasclass():
    return (peliculas_list)

@app.post("//", response_model=, status_code=status.HTTP_201_CREATED, response_description="El alumno se ha agregado")
async def (:):
    found=False
    
    for index, saved_ in enumerate():
        if saved_.id == .id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="El alumno ya existe")
    else:
        .append()
        return 
    
@app.put("//", response_model=, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion del alumno se ha actualizado")
async def (:):
    
    found=False

    for index, saved_ in enumerate():
        if saved_.id == .id:
            [index] = 
            found=True
    
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró al alumno con el ID")
    else:
        return , {"respuesta":"La informacion del alumno se actualizo!"}

@app.delete("//{id}", status_code=status.HTTP_202_ACCEPTED)
async def (id:int):
    
    found=False   
    
    for index, saved_ in enumerate():
        if saved_.id ==id:
           del [index] 
           found=True
           return "El alumno se elimino correctamente"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontro el alumno a eliminar")
        return {"message":"No se encontro el alumno a eliminar"}

    #1 Función para regresar el usuario completo de la base de datos (users_db), con contraseña encriptada
def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username]) #** devuelve todos los parámetros del usuario que coincida con username

#4 Función final para devolver usuario a la solicitud del backend   
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
    #3 Esta es la dependencia para buscar al usuario
async def auth_user(token:str=Depends(oauth2)):
    try:
        username= jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")

    return search_user(username) #Esta es la entrega final, usuario sin password

#2 Función para determinar si usuario esta inactivo 
async def current_user(user:User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user
        
####################################################################################3
        
@app.post("/login/")
async def login(form:OAuth2PasswordRequestForm= Depends()):
    #Busca en la base de datos "users_db" el username que se ingreso en la forma 
    user_db= users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    # Se obtienen los atributos incluyendo password del usuario que coincida el username de la forma 
    user= search_user_db(form.username)     
    
    #user.password es la contraseña encriptada en la base de datos
    #form.password es la contraseña original que viene en formulario
    if not crypt.verify(form.password,user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    #Creamos expiración de 1 min a partir de la hora actual
    access_token_expiration=timedelta(minutes=ACCESS_TOKEN_DURATION)
    #Tiempo de expiración: hora actual mas 1 minuto
    expire=datetime.utcnow()+access_token_expiration
    
    access_token={"sub": user.username,"exp": expire}
    return {"access_token": jwt.encode(access_token, SECRET,algorithm=ALGORITHM), "token_type":"bearer"}

@app.get("/users/me/")
async def me(user:User= Depends (current_user)): #Crea un user de tipo User que depende de la función (current_user)
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <link rel="stylesheet" href="../../static/styles.css">
        </head>
        <body>
            <div class="wrapper fadeInDown">
            <div id="formContent">
                <h2 class="active"> PERFIL DE USUARIO<h2>
                <div class="fadeIn first">
                    <img src="../../static/imagenes/""" + user.username + """.jpeg" id="img" alt="Imagenes de """ + user.username + """" />
                </div>
                <div>
                    <h2>Nombre:</h2>
                    <p> """ + user.full_name + """</p><br>
                    <h2>Email:</h2>
                    <p> """ + user.email + """</p><br>
                    <h2>Contacto:</h2>
                    <p> """ + user.phone + """</p><br>
                </div>
                <div id="formFooter">
                    <a class="underlineHover" href="#">Olvidaste tu contraseña</a>
                    <br></br>
                    <a class="underlineHover" href="#">Crear nuevo usuario</a>
                    <br></br>

                </div>
            </div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

#http://127.0.0.1:8000/login/

#username:Yosselin
#password:1234

#http://127.0.0.1:8000/users/me/