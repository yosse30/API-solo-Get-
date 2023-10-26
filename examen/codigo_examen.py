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

# generamos la contraseña encriptada para guardarla en base de datos
#https://bcrypt-generator.com/

#Levantamos el server Uvicorn
#-uvicorn actividad_jwt_auth_users:app --reload-

class User(BaseModel):
    username:str
    full_name: str
    email:str
    disabled:bool
    phone:str
    
  

#Definimos la clase para el usuario de base de datos 
class UserDB(User):
    password:str
    
#Creo una base de datos no relacional de usuarios 
users_db ={
     "Yosselin":{
         "username":"Yosselin",
         "full_name": "Yosselin Pablo",
         "email": "yosselin.pablo@alumno.buap.mx",
         "phone": "2288358188",
         "disabled": False,
         "password": "$2a$12$z3ZG4qGqQuQhMssUDR7FZ.55rNRpJqvSEo6fCn3RY83MiG3fIBadq" #"1234"
         
    },
    "Vicente":{
         "username":"Vicente",
         "full_name": "Vicente Zavaleta",
         "email": "vicente.zavaletas@alumno.buap.mx",
         "disabled": True,
         "phone": "2212671849",
         "password": "$2a$12$rKVsgkF5Xkkj3XZgne3Sgu3vEQctrSfcARxWddCnPXlzqh7dNlwZ6"#"5678"


    },

     "Pilar":{
         "username":"Pilar",
         "full_name": "Pilar Zambrano",
         "email": "pilar.hernandezz@alumno.buap.mx",
         "phone": "2223223454",
         "disabled": False,
         "password": "$2a$12$nv4bBkVoJzWWsb2Y88XFmueTDcLcyhZIkFybPb4Dzp0enkyzxyLlK" #"6789"

    },

    "Abraham":{
         "username":"Abraham",
         "full_name": "Abraham Temis",
         "email": "abraham.coagtle@alumno.buap.mx",
         "phone": "2731327748",
         "disabled": False,
         "password": "$2a$12$c0hg.am.Tv8ONgldnqtqlevr324.ovHYawChHbQu054M6/9.knVq." #"abcd"

    },

    "Victor":{
         "username":"Victor",
         "full_name": "Victor Manuel Zayas",
         "email": "victor.rosalesz@alumno.buap.mx",
         "phone": "2224415653",
         "disabled": True,
         "password": "$2a$12$ArYdjUR.a4AlDdW.CF1M.O05B4Xv1vgOCV5jlDgZlx9oLBgTuxUwG" #"efgh"

    },

    "Juan":{
         "username":"Juan",
         "full_name": "Juan Pablo Armas",
         "email": "juan.mendozaar@alumno.buap.mx",
         "phone": "2281776385",
         "disabled": False,
         "password": "$2a$12$GDuqarT0h1UBFJEd7dN2Ses6dJavV5Y17W666G.w0KCVKE1cE/ih." #"ijkl"


    },

    "Kevin":{
         "username":"Kevin",
         "full_name": "Kevin Hernandez",
         "email": "kevin.armas@alumno.buap.mx",
         "phone": "6141998990",
         "disabled": True,
         "password": "$2a$12$8kzZTKUDIsGXUGX6IgYOF.I6937fMgMzIHCHDLhLcM8vdUhTkTn1." #"mnño"


    },

    "Luis":{
         "username":"Luis",
         "full_name": "Luis Delfino Nava",
         "email": "luis.castron@alumno.buap.mx",
         "phone": "8110502639",
         "disabled": False,
         "password": "$2a$12$GUtKmoMh4RT3EUlQBeC78Of1WGYZAf8FFdvvSikXpvpwJSr4F5dwq" #"pqrs"

    },

    "Estefania":{
         "username":"Estefania",
         "full_name": "Estefania Martinez",
         "email": "estefania.rodriguezma@alumno.buap.mx",
         "phone": "2228669227",
         "disabled": True,
         "password": "$2a$12$v.Od37TaISt/LHce5L30JOIbFm1mAWx54gmiFpElhkYBMzGovzEBG" #"tuvw"

    },

    "Jose":{
         "username":"Jose",
         "full_name": "Jose Eduardo Alvarez",
         "email": "jose.arruchaal@alumno.buap.mx",
         "phone": "2213317079",
         "disabled": False,
         "password": "$2a$12$THUbw1FxB1On15H6zLLVfucEm3YxyVMWzwHkpjaBtWRDsthdnXfqS" #"1a2b"
         

         
    }

}

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

#-uvicorn codigo_examen:app --reload