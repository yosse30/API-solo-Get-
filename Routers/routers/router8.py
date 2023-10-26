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

peliculas_list= [Peliculas(id=1, marca="paramount", genero= "drama", año= 2019, titulo="Tully",clasificacion="R"),
                 Peliculas(id=2, marca="universal", genero="acción", año= 2019, titulo="Cazafantasmas",clasificacion="PG-13"),
                 Peliculas(id=3,marca= "20th century fox", genero= "fantasía", año= 2019, titulo="Los Nuevos Mutantes",clasificacion="PG-13"),
                 Peliculas(id=4,marca= "lionsgate", genero= "fantasía", año= 2019, titulo="Hellboy",clasificacion="R"),
                 Peliculas(id=5,marca= "paramount", genero= "ciencia ficción", año= 2019, titulo="Gemini Man",clasificacion="PG-13"),
                 Peliculas(id=6,marca= "columbia pictures", genero= "fantasía", año= 2019, titulo="Hombres de Negro",clasificacion="PG-13"),
                 Peliculas(id=7,marca= "disney", genero= "acción", año= 2019, titulo="Star Wars:El Ascenso de Skywalker",clasificacion="PG-13"),
                 Peliculas(id=8,marca= "universal", genero= "fantasía", año= 2019, titulo="Cats",clasificacion="PG"),
                 Peliculas(id=9,marca= "lionsgate", genero= "ciencia ficción", año=2019, titulo="Jugando con Fuego",clasificacion="PG"),
                 Peliculas(id=10,marca= "warner bros", genero= "animación", año= 2019, titulo="¡Shazam!",clasificacion="PG-13"),
                 Peliculas(id=11,marca= "paramount", genero= "animación", año= 2019, titulo="Dora and the Lost City of Gold",clasificacion="PG"),
                 Peliculas(id=12,marca="universal", genero= "comedia", año= 2019, titulo="Good Boys",clasificacion="R"),
                 Peliculas(id=13,marca= "lionsgate", genero= "romance", año= 2019, titulo="Five Feet Apart",clasificacion="PG-13"),
                 Peliculas(id=14,marca= "universal", genero= "acción", año= 2019, titulo="Fast & Furious Presents: Hobbs & Shaw",clasificacion="PG-13"),
                 Peliculas(id=15,marca= "lionsgate", genero= "animación", año= 2019, titulo="Wonder Park",clasificacion="PG"),
                 Peliculas(id=16,marca= "paramount", genero= "comedia", año= 2019, titulo="Booksmart",clasificacion="R"),
                 Peliculas(id=17,marca= "universal", genero= "romance", año= 2019, titulo="Yesterday",clasificacion="PG-13"),
                 Peliculas(id=19,marca= "paramount", genero= "acción", año= 2019, titulo="Terminator: Dark Fate",clasificacion="R"),
                 Peliculas(id=19,marca= "universal", genero= "animación", año= 2019, titulo="Abominable",clasificacion="PG"),
                 Peliculas(id=20,marca= "lionsgate", genero= "comedia", año= 2019, titulo="Long Shot",clasificacion="R"),
                 Peliculas(id=21,marca= "warner bros", genero= "animación", año= 2019, titulo="The Lego Movie 2",clasificacion="PG"),
                 Peliculas(id=22,marca= "lionsgate", genero="acción", año= 2019, titulo="John Wick:Chapter 3",clasificacion="R"),
                 Peliculas(id=23,marca= "columbia pictures", genero= "comedia", año= 2019, titulo="Once Upon an Time in Hollywood",clasificacion="R"),
                 Peliculas(id=24,marca= "warner bros", genero= "aventura", año= 2019, titulo="Pokemon Detective Picachu",clasificacion="PG"),
                 Peliculas(id=25,marca= "disney", genero= "animación", año= 2019, titulo="Frozen II",clasificacion="PG"),
                 Peliculas(id=26,marca= "disney", genero= "drama", año= 2019, titulo="El Rey Leon",clasificacion="PG")]

@router.get("/2019/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/2019/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La peliculas se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/2019/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizado")
async def peliculasclass(peliculas:Peliculas):
    
    found=False

    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            peliculas_list[index] = peliculas
            found=True
    
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró la peliculas con el ID")
    else:
        return peliculas, {"respuesta":"La informacion de la pelicula se actualizo!"}

@router.delete("/2019/{id}", status_code=status.HTTP_202_ACCEPTED)
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
       