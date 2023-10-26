from fastapi import FastAPI
#uvicorn Items_peliculas:app --reload
 

app= FastAPI()

 

peliculas= [

    {"marca": "sony", "genero": "ciencia ficción", "año": 2020},

    {"marca": "universal", "genero": "comedia", "año": 2018},

    {"marca": "paramount", "genero": "drama", "año": 2019},

    {"marca": "warner bros", "genero": "aventura", "año": 2017},

    {"marca": "20th century fox", "genero": "fantasía", "año": 2016},

    {"marca": "lionsgate", "genero": "animación", "año": 2014},

    {"marca": "disney", "genero": "musical", "año": 2021},

    {"marca": "dreamworks", "genero": "romance", "año": 2018},

    {"marca": "columbia pictures", "genero": "suspense", "año": 2017},

    {"marca": "universal", "genero": "acción", "año": 2019},

    {"marca": "sony", "genero": "ciencia ficción", "año": 2016},

    {"marca": "warner bros", "genero": "comedia", "año": 2015},

    {"marca": "paramount", "genero": "drama", "año":2018},

    {"marca": "disney", "genero": "aventura", "año": 2020},

    {"marca": "20th century fox", "genero": "fantasía", "año": 2019},

    {"marca": "lionsgate", "genero": "animación", "año": 2017},

    {"marca": "dreamworks", "genero": "musical", "año": 2015},

    {"marca": "columbia pictures", "genero": "romance", "año": 2014},

    {"marca": "universal", "genero": "suspense", "año": 2016},

    {"marca": "sony", "genero": "acción", "año": 2021},

    {"marca": "warner bros", "genero": "ciencia ficción", "año": 2017},

    {"marca": "paramount", "genero": "comedia", "año": 2016},

    {"marca": "disney", "genero": "drama", "año": 2015},

    {"marca": "20th century fox", "genero": "aventura", "año": 2020},

    {"marca": "lionsgate", "genero": "fantasía", "año": 2019},

    {"marca": "dreamworks", "genero": "animación", "año": 2018},

    {"marca": "columbia pictures", "genero": "musical", "año": 2017},

    {"marca": "universal", "genero": "romance", "año": 2016},

    {"marca": "sony", "genero": "suspense", "año": 2015},

    {"marca": "warner bros", "genero": "acción", "año": 2018},

    {"marca": "paramount", "genero": "ciencia ficción", "año": 2019},

    {"marca": "disney", "genero": "comedia", "año": 2017},

    {"marca": "20th century fox", "genero": "drama", "año": 2016},

    {"marca": "lionsgate", "genero": "aventura", "año": 2015},

    {"marca": "dreamworks", "genero": "fantasía", "año": 2021},

    {"marca": "columbia pictures", "genero": "animación", "año": 2020},

    {"marca": "universal", "genero": "musical", "año": 2018},

    {"marca": "sony", "genero": "romance", "año": 2017},

    {"marca": "warner bros", "genero": "suspense", "año": 2016},

    {"marca": "paramount", "genero": "acción", "año": 2015},

    {"marca": "disney", "genero": "ciencia ficción", "año": 2020},

    {"marca": "20th century fox", "genero": "comedia", "año": 2018},

    {"marca": "lionsgate", "genero": "drama", "año": 2017},

    {"marca": "dreamworks", "genero": "aventura", "año": 2015},

    {"marca": "columbia pictures", "genero": "fantasía", "año":2019},

    {"marca": "universal", "genero": "animación", "año": 2016},

    {"marca": "sony", "genero": "musical", "año": 2014},

    {"marca": "warner bros", "genero": "romance", "año":2021},

    {"marca": "paramount", "genero": "suspense", "año": 2020},

    {"marca": "disney", "genero": "acción", "año": 2019},

    {"marca": "20th century fox", "genero": "ciencia ficción", "año":2017},

    {"marca": "lionsgate", "genero": "comedia", "año": 2016},

    {"marca": "dreamworks", "genero": "drama", "año": 2015},

    {"marca": "columbia pictures", "genero": "aventura", "año": 2020},

    {"marca": "universal", "genero": "fantasía", "año": 2019},

    {"marca": "sony", "genero": "animación", "año": 2018},

    {"marca": "warner bros", "genero": "musical", "año": 2017},

    {"marca": "paramount", "genero": "romance", "año": 2016},

    {"marca": "disney", "genero": "suspense", "año": 2015},

    {"marca": "20th century fox", "genero": "acción", "año": 2018},

    {"marca": "lionsgate", "genero": "ciencia ficción", "año": 2019},

    {"marca": "dreamworks", "genero": "comedia", "año": 2017},

    {"marca": "columbia pictures", "genero": "drama", "año": 2016},

    {"marca": "universal", "genero": "aventura", "año": 2015},

    {"marca": "sony", "genero": "fantasía", "año": 2020},

    {"marca": "warner bros", "genero": "animación", "año": 2019},

    {"marca": "paramount", "genero": "musical", "año": 2017},

    {"marca": "disney", "genero": "romance", "año": 2016},

    {"marca": "20th century fox", "genero": "suspense", "año": 2015},

    {"marca": "lionsgate", "genero": "acción", "año": 2020},

    {"marca": "dreamworks", "genero": "ciencia ficción", "año": 2018},

    {"marca": "columbia pictures", "genero": "comedia", "año": 2017},

    {"marca": "universal", "genero": "drama", "año": 2016},

    {"marca": "sony", "genero": "aventura", "año": 2015},

    {"marca": "warner bros", "genero": "fantasía", "año": 2020},

    {"marca": "paramount", "genero": "animación", "año": 2019},

    {"marca": "disney", "genero": "musical", "año": 2018},

    {"marca": "20th century fox", "genero": "romance", "año": 2017},

    {"marca": "lionsgate", "genero": "suspense", "año": 2016},

    {"marca": "dreamworks", "genero": "acción", "año": 2015},

    {"marca": "columbia pictures", "genero": "ciencia ficción", "año": 2020},

    {"marca": "universal", "genero": "comedia", "año": 2019},

    {"marca": "sony", "genero": "drama", "año": 2018},

    {"marca": "warner bros", "genero": "aventura", "año": 2017},

    {"marca": "paramount", "genero": "fantasía", "año": 2016},

    {"marca": "disney", "genero": "animación", "año": 2015},

    {"marca": "20th century fox", "genero": "musical", "año": 2020},

    {"marca": "lionsgate", "genero": "romance", "año": 2019},

    {"marca": "dreamworks", "genero": "suspense", "año": 2018},

    {"marca": "columbia pictures", "genero": "acción", "año": 2017},

    {"marca": "universal", "genero": "ciencia ficción", "año": 2016},

    {"marca": "sony", "genero": "comedia", "año": 2015},

    {"marca": "warner bros", "genero": "drama", "año": 2020},

    {"marca": "paramount", "genero": "aventura", "año": 2019},

    {"marca": "disney", "genero": "fantasía", "año": 2018},

    {"marca": "20th century fox", "genero": "animación", "año": 2017},

    {"marca": "lionsgate", "genero": "musical", "año": 2016},

    {"marca": "dreamworks", "genero": "romance", "año": 2015},

    {"marca": "columbia pictures", "genero": "suspense", "año": 2020},

    {"marca": "universal", "genero": "acción", "año": 2019},

    {"marca": "sony", "genero": "ciencia ficción", "año": 2018},

    {"marca": "warner bros", "genero": "comedia", "año": 2017},

    {"marca": "paramount", "genero": "drama", "año": 2016},

    {"marca": "disney", "genero": "aventura", "año": 2015},

    {"marca": "20th century fox", "genero": "fantasía", "año": 2020},

    {"marca": "lionsgate", "genero": "animación", "año": 2019},

    {"marca": "dreamworks", "genero": "musical", "año": 2018},

    {"marca": "columbia pictures", "genero": "romance", "año": 2017},

    {"marca": "universal", "genero": "suspense", "año": 2016},

    {"marca": "sony", "genero": "acción", "año": 2015},

    {"marca": "warner bros", "genero": "ciencia ficción", "año": 2020},

    {"marca": "paramount", "genero": "comedia", "año": 2019},

    {"marca": "disney", "genero": "drama", "año": 2018},

    {"marca": "20th century fox", "genero": "aventura", "año": 2017},

    {"marca": "lionsgate", "genero": "fantasía", "año": 2016},

    {"marca": "dreamworks", "genero": "animación", "año": 2015},

    {"marca": "columbia pictures", "genero": "musical", "año": 2020},

    {"marca": "universal", "genero": "romance", "año": 2019},

    {"marca": "sony", "genero": "suspense", "año": 2018},

    {"marca": "warner bros", "genero": "acción", "año": 2017},

    {"marca": "paramount", "genero": "ciencia ficción", "año": 2016},

    {"marca": "disney", "genero": "comedia", "año": 2015},

    {"marca": "20th century fox", "genero": "drama", "año": 2020},

    {"marca": "lionsgate", "genero": "aventura", "año": 2019},

    {"marca": "dreamworks", "genero": "fantasía", "año": 2018},

    {"marca": "columbia pictures", "genero": "animación", "año": 2017},

    {"marca": "universal", "genero": "musical", "año": 2016},

    {"marca": "sony", "genero": "romance", "año": 2015},

    {"marca": "warner bros", "genero": "suspense", "año": 2020},

    {"marca": "paramount", "genero": "acción", "año": 2019},

    {"marca": "disney", "genero": "ciencia ficción", "año": 2018},

    {"marca": "20th century fox", "genero": "comedia", "año": 2017},

    {"marca": "lionsgate", "genero": "drama", "año": 2016},

    {"marca": "dreamworks", "genero": "aventura", "año": 2015},

    {"marca": "columbia pictures", "genero": "fantasía", "año": 2020},

    {"marca": "universal", "genero": "animación", "año": 2019},

    {"marca": "sony", "genero": "musical", "año": 2018},

    {"marca": "warner bros", "genero": "romance", "año": 2017},

    {"marca": "paramount", "genero": "suspense", "año": 2016},

    {"marca": "disney", "genero": "acción", "año": 2015},

    {"marca": "20th century fox", "genero": "ciencia ficción", "año": 2020},

    {"marca": "lionsgate", "genero": "comedia", "año": "2019"},

    {"marca": "dreamworks", "genero": "drama", "año": 2018},

    {"marca": "columbia pictures", "genero": "aventura", "año": 2017},

    {"marca": "universal", "genero": "fantasía", "año": 2016},

    {"marca": "sony", "genero": "animación", "año": 2015},

    {"marca": "warner bros", "genero": "musical", "año": 2020},

    {"marca": "paramount", "genero": "romance", "año": 2019},

    {"marca": "disney", "genero": "suspense", "año": 2018},

    {"marca": "20th century fox", "genero": "acción", "año": 2017},

    {"marca": "lionsgate", "genero": "ciencia ficción", "año": 2016},

    {"marca": "dreamworks", "genero": "comedia", "año": 2015},

    {"marca": "columbia pictures", "genero": "drama", "año": 2020},

    {"marca": "universal", "genero": "aventura", "año": 2019},

    {"marca": "sony", "genero": "fantasía", "año": 2018},

    {"marca": "warner bros", "genero": "animación", "año": 2017},

    {"marca": "paramount", "genero": "musical", "año": 2016},

    {"marca": "disney", "genero": "romance", "año":2015},

    {"marca": "20th century fox", "genero": "suspense", "año": 2020},

    {"marca": "lionsgate", "genero": "acción", "año": 2019},

    {"marca": "dreamworks", "genero": "ciencia ficción", "año": 2018},

    {"marca": "columbia pictures", "genero": "comedia", "año": 2017},

    {"marca": "universal", "genero": "drama", "año": 2016},

    {"marca": "sony", "genero": "aventura", "año": 2015},

    {"marca": "warner bros", "genero": "fantasía", "año": 2020},

    {"marca": "paramount", "genero": "animación", "año": 2019},

    {"marca": "disney", "genero": "musical", "año": 2018},

    {"marca": "20th century fox", "genero": "romance", "año": 2017},

    {"marca": "lionsgate", "genero": "suspense", "año": 2016},

    {"marca": "dreamworks", "genero": "acción", "año": 2015},

    {"marca": "columbia pictures", "genero": "ciencia ficción", "año": 2020},

    {"marca": "universal", "genero": "comedia", "año": 2019},

    {"marca": "sony", "genero": "drama", "año": 2018},

    {"marca": "warner bros", "genero": "aventura", "año": 2017},

    {"marca": "paramount", "genero": "fantasía", "año": 2016},

    {"marca": "disney", "genero": "animación", "año": 2015},

    {"marca": "universal", "genero": "acción", "año": 2015},

    {"marca": "paramount", "genero": "ciencia ficción", "año": 2016},

    {"marca": "warner bros", "genero": "comedia", "año": 2017},

    {"marca": "disney", "genero": "drama", "año": 2018},

    {"marca": "20th century fox", "genero": "aventura", "año": 2019},

    {"marca": "sony", "genero": "fantasía", "año": 2020},

    {"marca": "lionsgate", "genero": "animación", "año": 2021},

    {"marca": "dreamworks", "genero": "musical", "año": 2022},

    {"marca": "columbia pictures", "genero": "romance", "año": 2023},

    {"marca": "universal", "genero": "suspense", "año": 2024},

    {"marca": "paramount", "genero": "acción", "año": 2025},

    {"marca": "warner bros", "genero": "ciencia ficción", "año": 2026},

    {"marca": "disney", "genero": "comedia", "año": 2027},

    {"marca": "20th century fox", "genero": "drama", "año": 2028},

    {"marca": "sony", "genero": "aventura", "año": 2029},

    {"marca": "lionsgate", "genero": "fantasía", "año": 2030},

    {"marca": "dreamworks", "genero": "animación", "año": 2031},

    {"marca": "columbia pictures", "genero": "musical", "año": 2032},

    {"marca": "universal", "genero": "romance", "año": 2033},

    {"marca": "paramount", "genero": "suspense", "año": 2034},

    {"marca": "warner bros", "genero": "acción", "año": 2035},

    {"marca": "disney", "genero": "ciencia ficción", "año": 2036},

    {"marca": "20th century fox", "genero": "comedia", "año": 2037},

    {"marca": "sony", "genero": "drama", "año": 2038}

 

]

 

 

 

@app.get("/peliculas")

 

async def imprimir():

    return peliculas  #http://127.0.0.1:8000/peliculas/

 

 

@app.get("/peliculas/{marca}")
async def get_peliculas_by_marca(marca: str):
    filtered_peliculas = [pelicula for pelicula in peliculas if pelicula["marca"] == marca]
    return filtered_peliculas #http://127.0.0.1:8000/peliculas/sony

@app.get("/peliculas/marca/{genero}")
async def get_peliculas_by_genero(genero: str):
    filtered_peliculas = [pelicula for pelicula in peliculas if pelicula["genero"] == genero]
    return filtered_peliculas #http://127.0.0.1:8000/peliculas/marca/musical

@app.get("/peliculas/marca/genero/{año}")
async def get_peliculas_by_año(año: str):
    filtered_peliculas = [pelicula for pelicula in peliculas if pelicula["año"] == año]
    return filtered_peliculas #http://127.0.0.1:8000/peliculas/marca/genero/2015


