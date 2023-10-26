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

peliculas_list= [Peliculas(id=1, marca="universal", genero= "comedia", año= 2018, titulo="Mamma Mia! Vamos otra vez",clasificacion="PG-13"),
                 Peliculas(id=2, marca="universal", genero="acción", año= 2019, titulo="Cazafantasmas",clasificacion="PG-13"),
                 Peliculas(id=3,marca= "universal", genero= "suspense", año= 2016, titulo="Inferno",clasificacion="PG-13"),
                 Peliculas(id=4,marca= "universal", genero= "romance", año= 2016, titulo="Cincuenta Sombras Mas Oscuras",clasificacion="R"),
                 Peliculas(id=5,marca= "universal", genero= "musical", año= 2016, titulo="sing ¡Ven y Canta!",clasificacion="PG"),
                 Peliculas(id=6,marca= "universal", genero= "animación", año= 2016, titulo="¡Canta! (sing)",clasificacion="PG"),
                 Peliculas(id=7,marca= "universal", genero= "fantasía", año= 2019, titulo="Cats",clasificacion="PG"),
                 Peliculas(id=8,marca= "universal", genero= "aventura", año= 2015, titulo="Jurassic World",clasificacion="PG-13"),
                 Peliculas(id=9,marca= "universal", genero= "drama", año= 2016, titulo="Sully",clasificacion="PG-13"),
                 Peliculas(id=10,marca="universal", genero= "comedia", año= 2019, titulo="Good Boys",clasificacion="R"),
                 Peliculas(id=11,marca= "universal", genero= "ciencia ficción", año= 2016, titulo="Arrival",clasificacion="PG-13"),
                 Peliculas(id=12,marca= "universal", genero= "acción", año= 2019, titulo="Fast & Furious Presents: Hobbs & Shaw",clasificacion="PG-13"),
                 Peliculas(id=13,marca= "universal", genero= "suspense", año=2016, titulo="Passengers",clasificacion="R"),
                 Peliculas(id=14,marca= "universal", genero= "romance", año= 2019, titulo="Yesterday",clasificacion="PG-13"),
                 Peliculas(id=15,marca= "universal", genero= "musical", año= 2015, titulo="Straigth Outta Compton",clasificacion="R"),
                 Peliculas(id=16,marca= "universal", genero= "animación", año= 2019, titulo="Abominable",clasificacion="PG"),
                 Peliculas(id=17,marca= "universal", genero= "fantasía", año= 2016, titulo="The Huntsman: Winters War",clasificacion="PG-13"),
                 Peliculas(id=18,marca= "universal", genero= "aventura", año= 2020, titulo="The Call of the Wild",clasificacion="PG"),
                 Peliculas(id=19,marca= "universal", genero= "drama", año= 2016, titulo="Manchester by the Sea",clasificacion="R"),
                 Peliculas(id=20,marca= "universal", genero= "comedia", año= 2012, titulo="Ted",clasificacion="R"),
                 Peliculas(id=21,marca= "universal", genero= "acción", año= 2015, titulo="Rapido Y Furiosos 7",clasificacion="PG-13"),
                 Peliculas(id=22,marca= "universal", genero= "suspense", año= 2009, titulo="Duplicity",clasificacion="PG-13"),
                 Peliculas(id=23,marca= "universal", genero= "romance", año= 2013, titulo="About Time",clasificacion="R")]

@router.get("/universal/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/universal/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La peliculas se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/universal/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizado")
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

@router.delete("/universal/{id}", status_code=status.HTTP_202_ACCEPTED)
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