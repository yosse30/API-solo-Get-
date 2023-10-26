from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel

router= APIRouter()

class Peliculas (BaseModel):
    id:int
    marca:str
    genero:str
    año:int
    titulo:str
    clasificacion:str

peliculas_list= [Peliculas(id=1,marca= "warner bros", genero= "comedia", año= 2015, titulo="Alvin y las Ardillas: aventura sobre Ruedas",clasificacion="PG"),
                 Peliculas(id=2,marca= "dreamworks", genero= "musical", año= 2015, titulo="Home",clasificacion="PG"),
                 Peliculas(id=3,marca= "disney", genero= "drama", año= 2015, titulo="El Viaje de Arlo",clasificacion="PG"),
                 Peliculas(id=4,marca= "sony",genero="suspense", año= 2015, titulo="Sin Escape",clasificacion="R"),
                 Peliculas(id=5,marca= "lionsgate", genero= "aventura", año= 2015, titulo="Los Juegos del Hambre",clasificacion="PG-13"),
                 Peliculas(id=6,marca= "paramount", genero="acción", año= 2015, titulo="Mision Imposible",clasificacion="PG-13"),
                 Peliculas(id=7,marca= "dreamworks", genero= "aventura", año=2015, titulo="En Buen Dinosaurio",clasificacion="PG"),
                 Peliculas(id=8,marca= "dreamworks", genero= "drama", año= 2015, titulo="Bridge of Spies",clasificacion="PG-13"),
                 Peliculas(id=9,marca= "disney", genero= "Animacion", año= 2015, titulo="Intensa-Mente",clasificacion="PG"),
                 Peliculas(id=10,marca= "universal", genero= "aventura", año= 2015, titulo="Jurassic World",clasificacion="PG-13"),
                 Peliculas(id=11,marca= "20th century fox", genero= "suspense", año= 2015, titulo="The Martian",clasificacion="PG-13"),
                 Peliculas(id=12,marca= "sony", genero= "aventura", año= 2015, titulo="Goosebumps",clasificacion="PG"),
                 Peliculas(id=13,marca= "disney", genero= "animación", año= 2015, titulo="Bolt",clasificacion="PG"),
                 Peliculas(id=14,marca= "sony", genero= "comedia", año= 2015, titulo="The Nigth Before",clasificacion="R"),
                 Peliculas(id=15,marca= "dreamworks", genero= "romance", año= 2015, titulo="The Light Between Oceans",clasificacion="PG-13"),
                 Peliculas(id=16,marca="disney", genero= "aventura", año= 2015, titulo="Star Wars:Episode VII",clasificacion="PG-13"),
                 Peliculas(id=17,marca= "sony", genero= "acción", año= 2015, titulo="The Girl on the Train",clasificacion=""),
                 Peliculas(id=18,marca= "universal", genero= "musical", año= 2015, titulo="Straigth Outta Compton",clasificacion="R"),
                 Peliculas(id=19,marca= "sony", genero= "romance", año= 2015, titulo="Aloha",clasificacion="PG-13"),
                 Peliculas(id=20,marca= "disney", genero= "acción", año= 2015, titulo="Tomorrowlan",clasificacion="PG"),
                 Peliculas(id=21,marca= "sony", genero= "animación", año= 2015, titulo="Hotel Transylvana",clasificacion="PG"),
                 Peliculas(id=22,marca= "disney", genero= "romance", año= 2015, titulo="Cenicienta",clasificacion="PG"),
                 Peliculas(id=23,marca= "dreamworks", genero="ciencia ficción", año=2015, titulo="Chappie",clasificacion="R"),
                 Peliculas(id=24,marca= "sony", genero= "aventura", año= 2015, titulo="The Walk",clasificacion="PG"),
                 Peliculas(id=25,marca= "universal", genero= "acción", año= 2015, titulo="Rapido Y Furiosos 7",clasificacion="PG-13"),
                 Peliculas(id=26,marca= "20th century fox", genero= "comedia", año= 2015, titulo="Spy",clasificacion="R")]

@router.get("/2015/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/2015/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La pelicula se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/2015/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizado")
async def peliculasclass(peliculas:Peliculas):
    
    found=False

    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            peliculas_list[index] = peliculas
            found=True
    
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró la pelicula con el ID")
    else:
        return peliculas, {"respuesta":"La informacion de la pelicula se actualizo!"}

@router.delete("/2015/{id}", status_code=status.HTTP_202_ACCEPTED)
async def peliculasclass(id:int):
    
    found=False   
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id ==id:
           del peliculas_list[index] 
           found=True
           return "La pelicula se elimino correctamente"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontro la pelicula a eliminar")
        return {"message":"No se encontro la pelicula a eliminar"}