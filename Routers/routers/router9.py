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

peliculas_list= [Peliculas(id=1, marca="lionsgate", genero= "animación", año= 2014, titulo="El Principito",clasificacion="PG"),
                 Peliculas(id=2,marca= "lionsgate", genero= "animación", año= 2017, titulo="La Estrella De Belen",clasificacion="PG"),
                 Peliculas(id=3,marca="dreamworks", genero= "animación", año= 2018, titulo="Como Entrenar a tu Dragon 3",clasificacion="PG"),
                 Peliculas(id=4,marca="columbia pictures", genero= "animación", año= 2020, titulo="The Mitchells vs The Machines",clasificacion="PG"),
                 Peliculas(id=5,marca= "universal", genero= "animación", año= 2016, titulo="¡Canta! (sing)",clasificacion="PG"),
                 Peliculas(id=6,marca= "sony", genero= "animación", año= 2018, titulo="Spider-Man:Un Nuevo Universo",clasificacion="PG"),
                 Peliculas(id=7,marca= "warner bros", genero= "animación", año= 2019, titulo="¡Shazam!",clasificacion="PG-13"),
                 Peliculas(id=8,marca= "paramount", genero= "animación", año= 2019, titulo="Dora and the Lost City of Gold",clasificacion="PG"),
                 Peliculas(id=9,marca= "disney", genero= "animación", año= 2015, titulo="Bolt",clasificacion="PG"),
                 Peliculas(id=10,marca= "20th century fox", genero= "animación", año= 2017, titulo="Ferdinand",clasificacion="PG"),
                 Peliculas(id=11,marca= "lionsgate", genero= "animación", año= 2019, titulo="Wonder Park",clasificacion="PG"),
                 Peliculas(id=12,marca= "dreamworks", genero= "animación", año= 2013, titulo="Los Croods",clasificacion="PG"),
                 Peliculas(id=13,marca= "columbia pictures", genero= "animación", año= 2017, titulo="Emoji",clasificacion="PG"),
                 Peliculas(id=14,marca= "universal", genero= "animación", año= 2019, titulo="Abominable",clasificacion="PG"),
                 Peliculas(id=15,marca= "sony", genero= "animación", año= 2015, titulo="Hotel Transylvana",clasificacion="PG"),
                 Peliculas(id=16,marca= "warner bros", genero= "animación", año= 2019, titulo="The Lego Movie 2",clasificacion="PG"),
                 Peliculas(id=17,marca= "paramount", genero= "animación", año= 2011, titulo="Rango",clasificacion="PG"),
                 Peliculas(id=18,marca= "disney", genero= "animación", año= 2019, titulo="Frozen II",clasificacion="PG"),
                 Peliculas(id=19,marca= "lionsgate", genero= "animación", año= 2010, titulo="Alpha and Omega",clasificacion="PG"),
                 Peliculas(id=20,marca= "dreamworks", genero= "animación", año= 2007, titulo="Bee Movie",clasificacion="PG")]

@router.get("/animacion/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/animacion/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La peliculas se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/animacion/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizado")
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

@router.delete("/animacion/{id}", status_code=status.HTTP_202_ACCEPTED)
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