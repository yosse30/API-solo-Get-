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
                 Peliculas(id=2, marca="columbia pictures", genero= "suspense", año= 2017, titulo="Todavia Estamos Aqui",clasificacion="R"),
                 Peliculas(id=3,marca="sony", genero= "ciencia ficción", año= 2016, titulo="Morgan",clasificacion="R"),
                 Peliculas(id=4,marca= "warner bros", genero= "ciencia ficción", año= 2017, titulo="Blade Runner 2049",clasificacion="R"),
                 Peliculas(id=5,marca= "lionsgate", genero= "fantasía", año= 2019, titulo="Hellboy",clasificacion="R"),
                 Peliculas(id=6,marca= "universal", genero= "romance", año= 2016, titulo="Cincuenta Sombras Mas Oscuras",clasificacion="R"),
                 Peliculas(id=7,marca= "sony",genero="suspense", año= 2015, titulo="Sin Escape",clasificacion="R"),
                 Peliculas(id=8,marca= "20th century fox", genero= "drama", año= 2016, titulo="Paseo de la Fama",clasificacion="R"),
                 Peliculas(id=9,marca= "sony", genero= "romance", año= 2017, titulo="Baby Driver",clasificacion="R"),
                 Peliculas(id=10,marca= "20th century fox", genero= "comedia", año= 2018, titulo="Deadpool 2",clasificacion="R"),
                 Peliculas(id=11,marca= "warner bros", genero= "romance", año= 2021, titulo="The Suicide Squad",clasificacion="R"),
                 Peliculas(id=12,marca= "columbia pictures", genero= "aventura", año= 2020, titulo="Bad Boys for Lifes",clasificacion="R"),
                 Peliculas(id=13,marca= "paramount", genero= "romance", año= 2016, titulo="Allied",clasificacion="R"),
                 Peliculas(id=14,marca="universal", genero= "comedia", año= 2019, titulo="Good Boys",clasificacion="R"),
                 Peliculas(id=15,marca= "sony", genero= "drama", año= 2018, titulo="A Star is Born",clasificacion="R"),
                 Peliculas(id=16,marca= "dreamworks", genero= "suspense", año= 2013, titulo="The Fifth Estate",clasificacion="R"),
                 Peliculas(id=17,marca= "sony", genero= "comedia", año= 2015, titulo="The Nigth Before",clasificacion="R"),
                 Peliculas(id=18,marca= "lionsgate", genero= "musical", año= 2016, titulo="Hustle & Flow",clasificacion="R"),
                 Peliculas(id=19,marca= "columbia pictures", genero= "suspense", año= 2020, titulo="The Invisible Man",clasificacion="R"),
                 Peliculas(id=20,marca= "universal", genero= "suspense", año=2016, titulo="Passengers",clasificacion="R"),
                 Peliculas(id=21,marca= "paramount", genero= "comedia", año= 2019, titulo="Booksmart",clasificacion="R"),
                 Peliculas(id=22,marca= "20th century fox", genero= "aventura", año= 2017, titulo="Logan",clasificacion="R"),
                 Peliculas(id=23,marca= "sony", genero= "suspense", año= 2018, titulo="The Girl in the Spiders Web",clasificacion="R"),
                 Peliculas(id=24,marca= "20th century fox", genero= "drama", año= 2020, titulo="The Descendants",clasificacion="R"),
                 Peliculas(id=25,marca= "universal", genero= "musical", año= 2015, titulo="Straigth Outta Compton",clasificacion="R"),
                 Peliculas(id=26,marca= "paramount", genero= "acción", año= 2019, titulo="Terminator: Dark Fate",clasificacion="R"),
                 Peliculas(id=26,marca= "disney", genero= "acción", año= 2015, titulo="Tomorrowlan",clasificacion="PG"),
                 Peliculas(id=27,marca= "lionsgate", genero= "comedia", año= 2019, titulo="Long Shot",clasificacion="R"),
                 Peliculas(id=28,marca= "paramount", genero= "romance", año= 2017, titulo="Suburbircon",clasificacion="R"),
                 Peliculas(id=29,marca= "disney", genero= "suspense", año= 2018, titulo="Bad Times at The El Royale",clasificacion="R"),
                 Peliculas(id=30,marca= "lionsgate", genero= "ciencia ficción", año= 2016, titulo="Vivarium",clasificacion="R"),
                 Peliculas(id=31,marca= "20th century fox", genero= "suspense", año= 2006, titulo="Inside Man",clasificacion="R"),
                 Peliculas(id=32,marca= "lionsgate", genero="acción", año= 2019, titulo="John Wick:Chapter 3",clasificacion="R"),
                 Peliculas(id=33,marca= "dreamworks", genero="ciencia ficción", año=2015, titulo="Chappie",clasificacion="R"),
                 Peliculas(id=34,marca= "columbia pictures", genero= "comedia", año= 2019, titulo="Once Upon an Time in Hollywood",clasificacion="R"),
                 Peliculas(id=35,marca= "universal", genero= "drama", año= 2016, titulo="Manchester by the Sea",clasificacion="R"),
                 Peliculas(id=36,marca= "columbia pictures", genero= "ciencia ficción", año= 2017, titulo="Life",clasificacion="R"),
                 Peliculas(id=37,marca= "universal", genero= "comedia", año= 2012, titulo="Ted",clasificacion="R"),
                 Peliculas(id=38,marca= "sony", genero= "drama", año= 2018, titulo="The Wife" ,clasificacion="R"),
                 Peliculas(id=39,marca= "warner bros", genero= "comedia", año= 2011, titulo="The Hangover Part II",clasificacion="R"),
                 Peliculas(id=40,marca= "disney", genero= "drama", año= 2019, titulo="El Rey Leon",clasificacion="PG"),
                 Peliculas(id=41,marca= "sony", genero= "fantasía", año= 2020, titulo="The Green Knigth",clasificacion="R"),
                 Peliculas(id=42,marca= "universal", genero= "romance", año= 2013, titulo="About Time",clasificacion="R"),
                 Peliculas(id=43,marca= "paramount", genero= "suspense", año= 2018, titulo="Flight",clasificacion="R"),
                 Peliculas(id=44,marca= "20th century fox", genero= "comedia", año= 2015, titulo="Spy",clasificacion="R")]

@router.get("/R/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/R/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La peliculas se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/R/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizado")
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

@router.delete("/R/{id}", status_code=status.HTTP_202_ACCEPTED)
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