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
                 Peliculas(id=2, marca="20th century fox", genero= "fantasía", año= 2016, titulo="X-Men: Apocalipsis",clasificacion="PG-13"),
                 Peliculas(id=3, marca="lionsgate", genero= "animación", año= 2014, titulo="El Principito",clasificacion="PG-13"),
                 Peliculas(id=4, marca="dreamworks", genero= "romance", año= 2018, titulo="El Gran Amor de Beverly Hills",clasificacion="PG-13"),
                 Peliculas(id=5, marca="universal", genero="acción", año= 2019, titulo="Cazafantasmas",clasificacion="PG-13"),
                 Peliculas(id=6, marca= "paramount", genero= "drama", año= 2018, titulo="Bumblebee",clasificacion="PG-13"),
                 Peliculas(id=7,marca= "20th century fox", genero= "fantasía", año= 2019, titulo="Los Nuevos Mutantes",clasificacion="PG-13"),
                 Peliculas(id=8,marca= "universal", genero= "suspense", año= 2016, titulo="Inferno",clasificacion="PG-13"),
                 Peliculas(id=9,marca= "sony", genero= "acción", año= 2021, titulo="Un Lugar En Silencio",clasificacion="PG-13"),
                 Peliculas(id=10,marca= "paramount", genero="comedia", año= 2016, titulo="Zoolander 2",clasificacion="PG-13"),
                 Peliculas(id=11,marca= "columbia pictures", genero= "musical", año= 2017, titulo="Jumanji",clasificacion="PG-13"),
                 Peliculas(id=12,marca= "warner bros", genero= "acción", año=2018, titulo="Aquaman",clasificacion="PG-13"),
                 Peliculas(id=13,marca= "paramount", genero= "ciencia ficción", año= 2019, titulo="Gemini Man",clasificacion="PG-13"),
                 Peliculas(id=14,marca= "lionsgate", genero= "aventura", año= 2015, titulo="Los Juegos del Hambre",clasificacion="PG-13"),
                 Peliculas(id=15,marca= "paramount", genero="acción", año= 2015, titulo="Mision Imposible",clasificacion="PG-13"),
                 Peliculas(id=16,marca= "lionsgate", genero="drama", año= 2017, titulo="La La Land:Ciudad de Estrellas",clasificacion="PG-13"),
                 Peliculas(id=17,marca= "columbia pictures", genero= "fantasía", año= 2019, titulo="Hombres de Negro",clasificacion="PG-13"),
                 Peliculas(id=18,marca= "paramount", genero= "suspense", año= 2020, titulo="Un Lugar en Silencio:Parte II",clasificacion="PG-13"),
                 Peliculas(id=19,marca= "disney", genero= "acción", año= 2019, titulo="Star Wars:El Ascenso de Skywalker",clasificacion="PG-13"),
                 Peliculas(id=20,marca= "20th century fox", genero= "ciencia ficción", año= 2017, titulo="X-Men Fenix Oscura",clasificacion="PG-13"),
                 Peliculas(id=21,marca= "dreamworks", genero= "drama", año= 2015, titulo="Bridge of Spies",clasificacion="PG-13"),
                 Peliculas(id=22,marca= "20th century fox", genero= "drama", año= 2018, titulo="Bohemian Rhapsody",clasificacion="PG-13"),
                 Peliculas(id=23,marca="columbia pictures", genero= "drama", año= 2016, titulo="Infierno",clasificacion="PG-13"),
                 Peliculas(id=24,marca= "universal", genero= "aventura", año= 2015, titulo="Jurassic World",clasificacion="PG-13"),
                 Peliculas(id=25,marca= "warner bros", genero= "animación", año= 2019, titulo="¡Shazam!",clasificacion="PG-13"),
                 Peliculas(id=26,marca= "paramount", genero= "musical", año= 2017, titulo="Footloose",clasificacion="PG-13"),
                 Peliculas(id=27,marca= "20th century fox", genero= "suspense", año= 2015, titulo="The Martian",clasificacion="PG-13"),
                 Peliculas(id=28,marca= "lionsgate", genero= "acción", año= 2020, titulo="Greenland:El Ultimo Refugio",clasificacion="PG-13"),
                 Peliculas(id=29,marca= "dreamworks", genero= "ciencia ficción", año= 2018, titulo="Ready Playe One",clasificacion="PG-13"),
                 Peliculas(id=30,marca= "columbia pictures", genero= "comedia", año= 2012, titulo="The Amazing Spider-Man",clasificacion="PG-13"),
                 Peliculas(id=31,marca= "universal", genero= "drama", año= 2016, titulo="Sully",clasificacion="PG-13"),
                 Peliculas(id=32,marca= "warner bros", genero= "fantasía", año= 2020, titulo="Wonder Woman 1984",clasificacion="PG-13"),
                 Peliculas(id=33,marca= "20th century fox", genero= "romance", año= 2017, titulo="The Mountain Between Us",clasificacion="PG-13"),
                 Peliculas(id=34,marca= "lionsgate", genero= "suspense", año= 2016, titulo="Nerve",clasificacion="PG-13"),
                 Peliculas(id=35,marca= "dreamworks", genero="acción", año= 2011, titulo="Real Steel",clasificacion="PG-13"),
                 Peliculas(id=36,marca= "columbia pictures", genero= "ciencia ficción", año= 2020, titulo="Bloodshot",clasificacion="PG-13"),
                 Peliculas(id=37,marca= "warner bros", genero= "aventura", año=2017, titulo="Harry Potter and the Order of the Phoenix",clasificacion="PG-13"),
                 Peliculas(id=38,marca= "paramount", genero= "fantasía", año= 2016, titulo="Teenage Mutant Ninja Turtles: Out of the Shadows",clasificacion="PG-13"),
                 Peliculas(id=39,marca= "lionsgate", genero= "romance", año= 2019, titulo="Five Feet Apart",clasificacion="PG-13"),
                 Peliculas(id=40,marca= "columbia pictures", genero= "acción", año= 2007, titulo="Spider-Man 3",clasificacion="PG-13"),
                 Peliculas(id=41,marca= "universal", genero= "ciencia ficción", año= 2016, titulo="Arrival",clasificacion="PG-13"),
                 Peliculas(id=42,marca= "warner bros", genero= "drama", año= 2020, titulo="Tnet",clasificacion="PG-13"),
                 Peliculas(id=43,marca= "paramount", genero= "aventura", año= 2014, titulo="Transformers: Age of Extinction",clasificacion="PG-13"),
                 Peliculas(id=44,marca= "dreamworks", genero= "romance", año= 2015, titulo="The Light Between Oceans",clasificacion="PG-13"),
                 Peliculas(id=45,marca= "universal", genero= "acción", año= 2019, titulo="Fast & Furious Presents: Hobbs & Shaw",clasificacion="PG-13"),
                 Peliculas(id=46,marca= "sony", genero= "ciencia ficción", año= 2018, titulo="Venom",clasificacion="PG-13"),
                 Peliculas(id=47,marca= "paramount", genero= "drama", año= 2016, titulo="Fences",clasificacion="PG-13"),
                 Peliculas(id=48,marca="disney", genero= "aventura", año= 2015, titulo="Star Wars:Episode VII",clasificacion="PG-13"),
                 Peliculas(id=49,marca= "columbia pictures", genero= "romance", año= 2017, titulo= "",clasificacion="PG-13"),
                 Peliculas(id=50,marca= "warner bros", genero= "ciencia ficción", año= 2020, titulo="Ad Astra",clasificacion="PG-13"),
                 Peliculas(id=51,marca= "lionsgate", genero= "fantasía", año= 2016, titulo="Now You See Me 2",clasificacion="PG-13"),
                 Peliculas(id=52,marca= "dreamworks", genero= "animación", año= 2013, titulo="Los Croods",clasificacion="PG"),
                 Peliculas(id=53,marca= "columbia pictures", genero= "musical", año= 2005, titulo="Rent",clasificacion="PG-13"),
                 Peliculas(id=54,marca= "universal", genero= "romance", año= 2019, titulo="Yesterday",clasificacion="PG-13"),
                 Peliculas(id=55,marca= "warner bros", genero="acción", año=2017, titulo="Wonder Woman",clasificacion="PG-13"),
                 Peliculas(id=56,marca= "paramount", genero= "ciencia ficción", año= 2016, titulo="Terminator Genisys",clasificacion="PG-13"),
                 Peliculas(id=57,marca= "sony", genero= "romance", año= 2015, titulo="Aloha",clasificacion="PG-13"),
                 Peliculas(id=58,marca= "warner bros", genero= "suspense", año= 2020, titulo="Tenet",clasificacion="PG-13"),
                 Peliculas(id=59,marca= "lionsgate", genero= "drama", año= 2016, titulo="Midnigth Sun",clasificacion="PG-13"),
                 Peliculas(id=60,marca= "columbia pictures", genero= "fantasía", año= 2020, titulo="The Craft:Legacy",clasificacion="PG-13"),
                 Peliculas(id=61,marca= "warner bros", genero= "romance", año= 2017, titulo="Everything  Everything",clasificacion="PG-13"),
                 Peliculas(id=62,marca= "paramount", genero= "suspense", año= 2016, titulo="10 Cloverfield Lane",clasificacion="PG-13"),                 peliculas(id=141,marca= "20th century fox", genero= "ciencia ficción", año= "2020", titulo="The New Mutants",clasificacion="PG-13"),                 peliculas(id=143,marca= "dreamworks", genero= "drama", año= "2018", titulo="Green Book",clasificacion="PG-13"),
                 Peliculas(id=63,marca= "columbia pictures", genero= "aventura", año= 2014, titulo="The Amazing Spider-Man 2",clasificacion="PG-13"),
                 Peliculas(id=64,marca= "universal", genero= "fantasía", año= 2016, titulo="The Huntsman: Winters War",clasificacion="PG-13"),                 peliculas(id=147,marca= "warner bros", genero= "musical", año= "2020", titulo="In The Heigths",clasificacion="PG-13"), 
                 Peliculas(id=65,marca= "20th century fox", genero= "acción", año= 2017, titulo="War For The Planet of the Apes",clasificacion="PG-13"),
                 Peliculas(id=66,marca= "columbia pictures", genero= "drama", año= 2020, titulo="Greyhound",clasificacion="PG-13"),
                 Peliculas(id=67,marca= "paramount", genero= "musical", año= 2016, titulo="Florence Foster Jenkins",clasificacion="PG-13"),
                 Peliculas(id=68,marca= "warner bros", genero= "fantasía", año= 2013, titulo="The Hobbit",clasificacion="PG-13"),
                 Peliculas(id=69,marca= "20th century fox", genero= "romance", año= 2006, titulo="The Devil Wears Prada",clasificacion="PG-13"),
                 Peliculas(id=70,marca= "lionsgate", genero= "suspense", año= 2010, titulo="The Next Three Days",clasificacion="PG-13"),
                 Peliculas(id=71,marca= "dreamworks", genero= "acción", año= 2016, titulo="Deepwater Horizon",clasificacion="PG-13"),
                 Peliculas(id=72,marca= "universal", genero= "acción", año= 2015, titulo="Rapido Y Furiosos 7",clasificacion="PG-13"),
                 Peliculas(id=73,marca= "paramount", genero= "ciencia ficción", año= 2018, titulo="A Quiet Place",clasificacion="PG-13"),
                 Peliculas(id=74,marca= "columbia pictures", genero= "romance", año= 2011, titulo="Crazy Stupid Love" ,clasificacion="PG-13"),
                 Peliculas(id=75,marca= "universal", genero= "suspense", año= 2009, titulo="Duplicity",clasificacion="PG-13"),
                 Peliculas(id=76,marca= "paramount", genero= "acción", año= 2012, titulo="Gi Joe Retalation",clasificacion="PG-13"),
                 Peliculas(id=77,marca= "warner bros", genero= "ciencia ficción", año= 2014, titulo="Interstellar",clasificacion="PG-13"),
                 Peliculas(id=78,marca= "sony", genero= "aventura", año= 2020, titulo="Jumanji:The Next Level",clasificacion="PG-13"),
                 Peliculas(id=79,marca= "columbia pictures", genero= "musical", año= 2012, titulo="Les Miserables",clasificacion="PG-13"),
                 Peliculas(id=80,marca= "warner bros", genero= "acción", año= 2010, titulo="Inception",clasificacion="PG-13"),
                 Peliculas(id=81,marca= "disney", genero= "ciencia ficción", año= 2014, titulo="Guardians of the Galaxy",clasificacion="PG-13"),
                 Peliculas(id=82,marca= "sony", genero= "drama", año= 2021, titulo="The Father",clasificacion="PG-13")]

@router.get("/PG-13/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de peliculas exitosamente")
async def peliculasclass():
    return (peliculas_list)

@router.post("/PG-13/", response_model=Peliculas, status_code=status.HTTP_201_CREATED, response_description="La pelicula se ha agregado")
async def peliculasclass(peliculas:Peliculas):
    found=False
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La pelicula ya existe")
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
@router.put("/PG-13/", response_model=Peliculas, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la pelicula se ha actualizo")
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

@router.delete("/PG-13/{id}", status_code=status.HTTP_202_ACCEPTED)
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