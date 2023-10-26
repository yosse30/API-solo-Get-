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
                 Peliculas(id=3,marca= "disney", genero= "drama", año= 2015, titulo="El Viaje de Arlo",clasificacion="PG"),
                 Peliculas(id=4,marca= "20th century fox", genero= "drama", año= 2016, titulo="Paseo de la Fama",clasificacion="R"),
                 Peliculas(id=5,marca= "lionsgate", genero="drama", año= 2017, titulo="La La Land:Ciudad de Estrellas",clasificacion="PG-13"),
                 Peliculas(id=6,marca= "dreamworks", genero= "drama", año= 2015, titulo="Bridge of Spies",clasificacion="PG-13"),
                 Peliculas(id=7,marca= "20th century fox", genero= "drama", año= 2018, titulo="Bohemian Rhapsody",clasificacion="PG-13"),
                 Peliculas(id=8,marca="columbia pictures", genero= "drama", año= 2016, titulo="Infierno",clasificacion="PG-13"),
                 Peliculas(id=9,marca= "universal", genero= "drama", año= 2016, titulo="Sully",clasificacion="PG-13"),
                 Peliculas(id=10,marca= "sony", genero= "drama", año= 2018, titulo="A Star is Born",clasificacion="R"),
                 Peliculas(id=11,marca= "warner bros", genero= "drama", año= 2020, titulo="Tnet",clasificacion="PG-13"),
                 Peliculas(id=12,marca= "paramount", genero= "drama", año= 2016, titulo="Fences",clasificacion="PG-13"),
                 Peliculas(id=13,marca= "disney", genero= "drama", año= 2010, titulo="Secretariat",clasificacion="PG"),
                 Peliculas(id=14,marca= "20th century fox", genero= "drama", año= 2020, titulo="The Descendants",clasificacion="R"),
                 Peliculas(id=15,marca= "lionsgate", genero= "drama", año= 2016, titulo="Midnigth Sun",clasificacion="PG-13"),
                 Peliculas(id=16,marca= "dreamworks", genero= "drama", año= 2018, titulo="Green Book",clasificacion="PG-13"),
                 Peliculas(id=17,marca= "columbia pictures", genero= "drama", año= 2020, titulo="Greyhound",clasificacion="PG-13"),
                 Peliculas(id=18,marca= "universal", genero= "drama", año= 2016, titulo="Manchester by the Sea",clasificacion="R"),
                 Peliculas(id=19,marca= "sony", genero= "drama", año= 2018, titulo="The Wife" ,clasificacion="R"),
                 Peliculas(id=20,marca= "disney", genero= "drama", año= 2019, titulo="El Rey Leon",clasificacion="PG"),
                 Peliculas(id=21,marca= "20th century fox", genero= "drama", año= 2012, titulo="Life Of Pi",clasificacion="PG"),
                 Peliculas(id=22,marca= "sony", genero= "drama", año= 2021, titulo="The Father",clasificacion="PG-13")]

@router.get("/drama/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/drama/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La pelicula se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/drama/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizado")
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

@router.delete("/drama/{id}", status_code=status.HTTP_202_ACCEPTED)
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