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
                 Peliculas(id=2,marca= "warner bros", genero= "comedia", año= 2015, titulo="Alvin y las Ardillas: aventura sobre Ruedas",clasificacion="PG"),
                 Peliculas(id=3,marca= "paramount", genero="comedia", año= 2016, titulo="Zoolander 2",clasificacion="PG-13"),
                 Peliculas(id=4,marca= "disney", genero= "comedia", año= 2017, titulo="Coco",clasificacion="PG"),
                 Peliculas(id=5,marca= "20th century fox", genero= "comedia", año= 2018, titulo="Deadpool 2",clasificacion="R"),
                 Peliculas(id=6,marca= "lionsgate", genero= "comedia", año= 2016, titulo="¡Madicion Otra Vez Navidad!",clasificacion="PG"),
                 Peliculas(id=7,marca= "dreamworks", genero= "comedia", año= 2017, titulo="The Boss Baby",clasificacion="PG"),
                 Peliculas(id=8,marca= "columbia pictures", genero= "comedia", año= 2012, titulo="The Amazing Spider-Man",clasificacion="PG-13"),
                 Peliculas(id=9,marca="universal", genero= "comedia", año= 2019, titulo="Good Boys",clasificacion="R"),
                 Peliculas(id=10,marca= "sony", genero= "comedia", año= 2015, titulo="The Nigth Before",clasificacion="R"),
                 Peliculas(id=11,marca= "warner bros", genero= "comedia", año= 2017, titulo="The Lego Batman Movie",clasificacion="PG"),
                 Peliculas(id=12,marca= "paramount", genero= "comedia", año= 2019, titulo="Booksmart",clasificacion="R"),
                 Peliculas(id=13,marca= "disney", genero= "comedia", año= 2012, titulo= "Wreck It-Ralph",clasificacion="PG"),
                 Peliculas(id=14,marca= "20th century fox", genero="comedia", año= 2017, titulo="Diary of a Wimpy Kid",clasificacion="PG"),
                 Peliculas(id=15,marca= "lionsgate", genero= "comedia", año= 2019, titulo="Long Shot",clasificacion="R"),
                 Peliculas(id=16,marca= "dreamworks", genero= "comedia", año= 2012, titulo="Madadascar 3",clasificacion="PG"),
                 Peliculas(id=17,marca= "columbia pictures", genero= "comedia", año= 2019, titulo="Once Upon an Time in Hollywood",clasificacion="R"),
                 Peliculas(id=18,marca= "universal", genero= "comedia", año= "2012", titulo="Ted",clasificacion="R"),
                 Peliculas(id=19,marca= "warner bros", genero= "comedia", año= "2011", titulo="The Hangover Part II",clasificacion="R"),
                 Peliculas(id=20,marca= "disney", genero= "comedia", año= "2017", titulo="Cars 3",clasificacion="PG"),
                 Peliculas(id=21,marca= "20th century fox", genero= "comedia", año= "2015", titulo="Spy",clasificacion="R")]

@router.get("/comedia/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/comedia/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La pelicula se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/comedia/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizado")
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

@router.delete("/comedia/{id}", status_code=status.HTTP_202_ACCEPTED)
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