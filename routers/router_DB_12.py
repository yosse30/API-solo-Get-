#Acciones
#1 cambiamos path de "usersclass" a "userdb"
#Movemos basemodel
#vaciamos user list

#-uvicorn main:app --reload-

#Path:  http://127.0.0.1:8000/userdb

#POST-body-JSON
#{


#En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException
#Invocamos la entidad que hemos creado ****nEw
from db.models.user3 import User
#Importamos la instancia que devolvera al usuario en formato user ***new
from db.schemas.user3 import user_schema
#Importamos nuestro cliente para poder agregar usuarios a la db****nEw
from db.client_11 import db_client




#Creamos un objeto a partir de la clase FastAPI
router= APIRouter()

#Levantamos el server Uvicorn
#-uvicorn 4_codigos_HTTP:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: user


#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  




 #***Get Todos los Usuarios
@router.get("/userdb3/")
async def usersclass():
    users = list(db_client.actividad10.peliculas.find())
    schema = [user_schema(user) for user in users]
    return schema

#***Get Usuario por ID
@router.get("/userdb3/{user_marca}")
async def get_user(user_marca: str):
    user = db_client.actividad10.peliculas.find_one({"marca": user_marca})
    if user:
        return user_schema(user)
    else:
        raise HTTPException(status_code=404, detail="User not found")

#***Get con Filtro Query (por ejemplo, http://127.0.0.1:8000/userdb/?id=1)
@router.get("/userdb3/")
async def get_user_by_query(marca: str):
    user = db_client.actividad10.peliculas.find_one({"marca": marca})
    if user:
        return user_schema(user)
    else:
        raise HTTPException(status_code=404, detail="User not found")
 
 
#***Post
@router.post("/userdb3/",response_model=User, status_code=201)
async def userdb3(user:User):
    
    #2Transformo mi entidad user en un diccionario. Transformo User en diccionario
    user_dict= dict (user)
    #Elimino id del diccionario
    del user_dict["id"]
    #1 Creo un esquema que se llama usuarios dentro de Computacion
    #Computación= Base de datos
    #users= Colección o esquema
    id= db_client.actividad10.peliculas.insert_one(user_dict).inserted_id
    
    #Consultamos el user insertado en la bd con todo y id asignado automaticamente
    #Me devuelve un JSON hay que convertirlo a un objeto tipo User (user.py en schemas)
    new_user=  user_schema(db_client.actividad10.peliculas.find_one({"_id":id}))
    
    #La base de datos devuelve un JSON debemos transformarlo a un objeto tipo user:
    return User(**new_user)
    

    #***Put
@router.put("/userdb3/{user_marca}")
async def update_user(user_marca: str, updated_user: User):
    # Verificamos si el usuario existe
    existing_user = db_client.actividad10.peliculas.find_one({"marca": user_marca})
    
    if existing_user:
        # Eliminamos el ID del usuario actualizado
        del updated_user.marca

        # Actualizamos el usuario en la base de datos
        result = db_client.actividad10.peliculas.update_one({"marca": user_marca}, {"$set": updated_user.dict()})
        
        if result.modified_count == 1:
            return {"message": "User updated successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to update user")
    else:
        raise HTTPException(status_code=404, detail="User not found")

    #http://127.0.0.1:8000/usersclass/
    
    
    #***Delete
@router.delete("/userdb3/{marca}")
async def delete_user(marca: str):
    result = db_client.actividad9.peliculas.delete_one({"id": id})
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

    
    #http://127.0.0.1:8000/usersclass/1