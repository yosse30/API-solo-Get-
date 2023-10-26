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
                 Peliculas(id=2, marca= "paramount", genero= "drama", año= 2018, titulo="Bumblebee",clasificacion="PG-13"),
                 Peliculas(id=3,marca= "paramount", genero="comedia", año= 2016, titulo="Zoolander 2",clasificacion="PG-13"),
                 Peliculas(id=4,marca= "paramount", genero= "ciencia ficción", año= 2019, titulo="Gemini Man",clasificacion="PG-13"),
                 Peliculas(id=5,marca= "paramount", genero="acción", año= 2015, titulo="Mision Imposible",clasificacion="PG-13"),
                 Peliculas(id=6,marca= "paramount", genero= "suspense", año= 2020, titulo="Un Lugar en Silencio:Parte II",clasificacion="PG-13"),
                 Peliculas(id=7,marca= "paramount", genero= "romance", año= 2016, titulo="Allied",clasificacion="R"),
                 Peliculas(id=8,marca= "paramount", genero= "musical", año= 2017, titulo="Footloose",clasificacion="PG-13"),
                 Peliculas(id=9,marca= "paramount", genero= "animación", año= 2019, titulo="Dora and the Lost City of Gold",clasificacion="PG"),
                 Peliculas(id=10,marca= "paramount", genero= "fantasía", año= 2016, titulo="Teenage Mutant Ninja Turtles: Out of the Shadows",clasificacion="PG-13"),
                 Peliculas(id=11,marca= "paramount", genero= "aventura", año= 2014, titulo="Transformers: Age of Extinction",clasificacion="PG-13"),
                 Peliculas(id=12,marca= "paramount", genero= "drama", año= 2016, titulo="Fences",clasificacion="PG-13"),
                 Peliculas(id=13,marca= "paramount", genero= "comedia", año= 2019, titulo="Booksmart",clasificacion="R"),
                 Peliculas(id=14,marca= "paramount", genero= "ciencia ficción", año= 2016, titulo="Terminator Genisys",clasificacion="PG-13"),
                 Peliculas(id=15,marca= "paramount", genero= "acción", año= 2019, titulo="Terminator: Dark Fate",clasificacion="R"),
                 Peliculas(id=16,marca= "paramount", genero= "suspense", año= 2016, titulo="10 Cloverfield Lane",clasificacion="PG-13"),
                 Peliculas(id=17,marca= "paramount", genero= "romance", año= 2017, titulo="Suburbircon",clasificacion="R"),
                 Peliculas(id=18,marca= "paramount", genero= "musical", año= 2016, titulo="Florence Foster Jenkins",clasificacion="PG-13"),
                 Peliculas(id=19,marca= "paramount", genero= "animación", año= 2011, titulo="Rango",clasificacion="PG"),
                 Peliculas(id=20,marca= "paramount", genero= "fantasía", año= 2016, titulo="Monster Trucks",clasificacion="PG"),
                 Peliculas(id=21,marca= "paramount", genero= "ciencia ficción", año= 2018, titulo="A Quiet Place",clasificacion="PG-13"),
                 Peliculas(id=22,marca= "paramount", genero= "acción", año= 2012, titulo="Gi Joe Retalation",clasificacion="PG-13"),
                 Peliculas(id=23,marca= "paramount", genero= "suspense", año= 2018, titulo="Flight",clasificacion="R")]

@router.get("/paramount/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/paramount/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La peliculas se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/paramount/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizado")
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

@router.delete("/paramount/{id}", status_code=status.HTTP_202_ACCEPTED)
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