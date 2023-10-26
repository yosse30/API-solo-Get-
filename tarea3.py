from fastapi import FastAPI

from pydantic import BaseModel

app= FastAPI()

class peliculas (BaseModel):
    id:int
    marca:str
    genero:str
    año:int
    titulo:str
    clasificacion:str

peliculas_list= [peliculas(id=1, marca="universal", genero= "comedia", año= 2018, titulo="Mamma Mia! Vamos otra vez",clasificacion="PG-13"),
                 peliculas(id=2, marca="paramount", genero= "drama", año= 2019, titulo="Tully",clasificacion="R"),
                 peliculas(id=3, marca="warner bros", genero= "aventura", año= 2017, titulo="LEGO Batman",clasificacion="PG"),
                 peliculas(id=4, marca="20th century fox", genero= "fantasía", año= 2016, titulo="X-Men: Apocalipsis",clasificacion="PG-13"),
                 peliculas(id=5, marca="lionsgate", genero= "animación", año= 2014, titulo="El Principito",clasificacion="PG"),
                 peliculas(id=6, marca="disney", genero= "musical", año= 2021, titulo="Encanto",clasificacion="PG"),
                 peliculas(id=7, marca="dreamworks", genero= "romance", año= 2018, titulo="El Gran Amor de Beverly Hills",clasificacion="PG-13"),
                 peliculas(id=8, marca="columbia pictures", genero= "suspense", año= 2017, titulo="Todavia Estamos Aqui",clasificacion="R"),
                 peliculas(id=9, marca="universal", genero="acción", año= 2019, titulo="Cazafantasmas",clasificacion="PG-13"),
                 peliculas(id=10,marca="sony", genero= "ciencia ficción", año= 2016, titulo="Morgan",clasificacion="R"),
                 peliculas(id=11,marca= "warner bros", genero= "comedia", año= 2015, titulo="Alvin y las Ardillas: aventura sobre Ruedas",clasificacion="PG"),
                 peliculas(id=12, marca= "paramount", genero= "drama", año= 2018, titulo="Bumblebee",clasificacion="PG-13"),
                 peliculas(id=13, marca= "disney", genero= "aventura", año= 2020, titulo="Onward",clasificacion="PG"),
                 peliculas(id=14,marca= "20th century fox", genero= "fantasía", año= 2019, titulo="Los Nuevos Mutantes",clasificacion="PG-13"),
                 peliculas(id=15,marca= "lionsgate", genero= "animación", año= 2017, titulo="La Estrella De Belen",clasificacion="PG"),
                 peliculas(id=16,marca= "dreamworks", genero= "musical", año= 2015, titulo="Home",clasificacion="PG"),
                 peliculas(id=17,marca= "columbia pictures", genero="romance", año= 2014, titulo="Anni",clasificacion="PG"),
                 peliculas(id=18,marca= "universal", genero= "suspense", año= 2016, titulo="Inferno",clasificacion="PG-13"),
                 peliculas(id=19,marca= "sony", genero= "acción", año= 2021, titulo="Un Lugar En Silencio",clasificacion="PG-13"),
                 peliculas(id=20,marca= "warner bros", genero= "ciencia ficción", año= 2017, titulo="Blade Runner 2049",clasificacion="R"),
                 peliculas(id=21,marca= "paramount", genero="comedia", año= 2016, titulo="Zoolander 2",clasificacion="PG-13"),
                 peliculas(id=22,marca= "disney", genero= "drama", año= 2015, titulo="El Viaje de Arlo",clasificacion="PG"),
                 peliculas(id=23,marca= "20th century fox", genero= "aventura", año= 2020, titulo="La Llama de lo Salvaje",clasificacion="PG"),
                 peliculas(id=24,marca= "lionsgate", genero= "fantasía", año= 2019, titulo="Hellboy",clasificacion="R"),
                 peliculas(id=25,marca="dreamworks", genero= "animación", año= 2018, titulo="Como Entrenar a tu Dragon 3",clasificacion="PG"),
                 peliculas(id=26,marca= "columbia pictures", genero= "musical", año= 2017, titulo="Jumanji",clasificacion="PG-13"),
                 peliculas(id=27,marca= "universal", genero= "romance", año= 2016, titulo="Cincuenta Sombras Mas Oscuras",clasificacion="R"),
                 peliculas(id=28,marca= "sony",genero="suspense", año= 2015, titulo="Sin Escape",clasificacion="R"),
                 peliculas(id=29,marca= "warner bros", genero= "acción", año=2018, titulo="Aquaman",clasificacion="PG-13"),
                 peliculas(id=30,marca= "paramount", genero= "ciencia ficción", año= 2019, titulo="Gemini Man",clasificacion="PG-13"),
                 peliculas(id=31,marca= "disney", genero= "comedia", año= 2017, titulo="Coco",clasificacion="PG"),
                 peliculas(id=32,marca= "20th century fox", genero= "drama", año= 2016, titulo="Paseo de la Fama",clasificacion="R"),
                 peliculas(id=33,marca= "lionsgate", genero= "aventura", año= 2015, titulo="Los Juegos del Hambre",clasificacion="PG-13"),
                 peliculas(id=34,marca= "dreamworks", genero= "fantasía", año= 2014, titulo="Como Entregar a tu Dragon 2",clasificacion= "PG"),
                 peliculas(id=35,marca="columbia pictures", genero= "animación", año= 2020, titulo="The Mitchells vs The Machines",clasificacion="PG"),
                 peliculas(id=36,marca= "universal", genero= "musical", año= 2016, titulo="sing ¡Ven y Canta!",clasificacion="PG"),
                 peliculas(id=37,marca= "sony", genero= "romance", año= 2017, titulo="Baby Driver",clasificacion="R"),
                 peliculas(id=38,marca= "warner bros", genero= "suspense", año= 2016, titulo="El Contador",clasificacion="R"),
                 peliculas(id=39,marca= "paramount", genero="acción", año= 2015, titulo="Mision Imposible",clasificacion="PG-13"),
                 peliculas(id=40,marca= "disney", genero= "ciencia ficción", año=2020, titulo="Artemis Fowl",clasificacion="PG"),
                 peliculas(id=41,marca= "20th century fox", genero= "comedia", año= 2018, titulo="Deadpool 2",clasificacion="R"),
                 peliculas(id=42,marca= "lionsgate", genero="drama", año= 2017, titulo="La La Land:Ciudad de Estrellas",clasificacion="PG-13"),
                 peliculas(id=43,marca= "dreamworks", genero= "aventura", año=2015, titulo="En Buen Dinosaurio",clasificacion="PG"),
                 peliculas(id=44,marca= "columbia pictures", genero= "fantasía", año= 2019, titulo="Hombres de Negro",clasificacion="PG-13"),
                 peliculas(id=45,marca= "universal", genero= "animación", año= 2016, titulo="¡Canta! (sing)",clasificacion="PG"),
                 peliculas(id=46,marca= "sony", genero= "musical", año= 2014, titulo="Annie",clasificacion="PG"),
                 peliculas(id=47,marca= "warner bros", genero= "romance", año= 2021, titulo="The Suicide Squad",clasificacion="R"),
                 peliculas(id=48,marca= "paramount", genero= "suspense", año= 2020, titulo="Un Lugar en Silencio:Parte II",clasificacion="PG-13"),
                 peliculas(id=49,marca= "disney", genero= "acción", año= 2019, titulo="Star Wars:El Ascenso de Skywalker",clasificacion="PG-13"),
                 peliculas(id=50,marca= "20th century fox", genero= "ciencia ficción", año= 2017, titulo="X-Men Fenix Oscura",clasificacion="PG-13"),
                 peliculas(id=51,marca= "lionsgate", genero= "comedia", año= 2016, titulo="¡Madicion Otra Vez Navidad!",clasificacion="PG"),
                 peliculas(id=52,marca= "dreamworks", genero= "drama", año= 2015, titulo="Bridge of Spies",clasificacion="PG-13"),
                 peliculas(id=53,marca= "columbia pictures", genero= "aventura", año= 2020, titulo="Bad Boys for Lifes",clasificacion="R"),
                 peliculas(id=54,marca= "universal", genero= "fantasía", año= 2019, titulo="Cats",clasificacion="PG"),
                 peliculas(id=55,marca= "sony", genero= "animación", año= 2018, titulo="Spider-Man:Un Nuevo Universo",clasificacion="PG"),
                 peliculas(id=56,marca= "warner bros", genero= "musical", año= 2017, titulo="El Gran Showman",clasificacion="PG"),
                 peliculas(id=57,marca= "paramount", genero= "romance", año= 2016, titulo="Allied",clasificacion="R"),
                 peliculas(id=58,marca= "disney", genero= "Animacion", año= 2015, titulo="Intensa-Mente",clasificacion="PG"),
                 peliculas(id=59,marca= "20th century fox", genero= "drama", año= 2018, titulo="Bohemian Rhapsody",clasificacion="PG-13"),
                 peliculas(id=60,marca= "lionsgate", genero= "ciencia ficción", año=2019, titulo="Jugando con Fuego",clasificacion="PG"),
                 peliculas(id=61,marca= "dreamworks", genero= "comedia", año= 2017, titulo="The Boss Baby",clasificacion="PG"),
                 peliculas(id=62,marca="columbia pictures", genero= "drama", año= 2016, titulo="Infierno",clasificacion="PG-13"),
                 peliculas(id=63,marca= "universal", genero= "aventura", año= 2015, titulo="Jurassic World",clasificacion="PG-13"),
                 peliculas(id=64,marca= "sony", genero= "fantasía", año= 2020, titulo="The Witches",clasificacion="PG"),
                 peliculas(id=65,marca= "warner bros", genero= "animación", año=2019, titulo="¡Shazam!",clasificacion="PG-13"),
                 peliculas(id=66,marca= "paramount", genero= "musical", año= 2017, titulo="Footloose",clasificacion="PG-13"),
                 peliculas(id=67,marca= "disney", genero= "romance", año= 2018, titulo="Christopher Robin",clasificacion="PG"),
                 peliculas(id=68,marca= "20th century fox", genero= "suspense", año= 2015, titulo="The Martian",clasificacion="PG-13"),
                 peliculas(id=69,marca= "lionsgate", genero= "acción", año= 2020, titulo="Greenland:El Ultimo Refugio",clasificacion="PG-13"),
                 peliculas(id=70,marca= "dreamworks", genero= "ciencia ficción", año= 2018, titulo="Ready Playe One",clasificacion="PG-13"),
                 peliculas(id=71,marca= "columbia pictures", genero= "comedia", año= 2012, titulo="The Amazing Spider-Man",clasificacion="PG-13"),
                 peliculas(id=72,marca= "universal", genero= "drama", año= 2016, titulo="Sully",clasificacion="PG-13"),
                 peliculas(id=73,marca= "sony", genero= "aventura", año= 2015, titulo="Goosebumps",clasificacion="PG"),
                 peliculas(id=74,marca= "warner bros", genero= "fantasía", año= 2020, titulo="Wonder Woman 1984",clasificacion="PG-13"),
                 peliculas(id=75,marca= "paramount", genero= "animación", año=2019, titulo="Dora and the Lost City of Gold",clasificacion="PG"),
                 peliculas(id=76,marca= "disney", genero= "musical", año= 2018, titulo="Mary Poppins Return",clasificacion="PG"),
                 peliculas(id=77,marca= "20th century fox", genero= "romance", año= 2017, titulo="The Mountain Between Us",clasificacion="PG-13"),
                 peliculas(id=78,marca= "lionsgate", genero= "suspense", año= 2016, titulo="Nerve",clasificacion="PG-13"),
                 peliculas(id=79,marca= "dreamworks", genero="acción", año= 2011, titulo="Real Steel",clasificacion="PG-13"),
                 peliculas(id=80,marca= "columbia pictures", genero= "ciencia ficción", año= 2020, titulo="Bloodshot",clasificacion="PG-13"),
                 peliculas(id=81,marca="universal", genero= "comedia", año= 2019, titulo="Good Boys",clasificacion="R"),
                 peliculas(id=82,marca= "sony", genero= "drama", año= 2018, titulo="A Star is Born",clasificacion="R"),
                 peliculas(id=83,marca= "warner bros", genero= "aventura", año=2017, titulo="Harry Potter and the Order of the Phoenix",clasificacion="PG-13"),
                 peliculas(id=84,marca= "paramount", genero= "fantasía", año= 2016, titulo="Teenage Mutant Ninja Turtles: Out of the Shadows",clasificacion="PG-13"),
                 peliculas(id=85,marca= "disney", genero= "animación", año= 2015, titulo="Bolt",clasificacion="PG"),
                 peliculas(id=86,marca= "20th century fox", genero= "musical", año= 2020, titulo="Glee: The 3D Concert Movie",clasificacion="PG"),
                 peliculas(id=87,marca= "lionsgate", genero= "romance", año= 2019, titulo="Five Feet Apart",clasificacion="PG-13"),
                 peliculas(id=88,marca= "dreamworks", genero= "suspense", año= 2013, titulo="The Fifth Estate",clasificacion="R"),
                 peliculas(id=89,marca= "columbia pictures", genero= "acción", año= 2007, titulo="Spider-Man 3",clasificacion="PG-13"),
                 peliculas(id=90,marca= "universal", genero= "ciencia ficción", año= 2016, titulo="Arrival",clasificacion="PG-13"),
                 peliculas(id=91,marca= "sony", genero= "comedia", año= 2015, titulo="The Nigth Before",clasificacion="R"),
                 peliculas(id=92,marca= "warner bros", genero= "drama", año= 2020, titulo="Tnet",clasificacion="PG-13"),
                 peliculas(id=93,marca= "paramount", genero= "aventura", año=2014, titulo="Transformers: Age of Extinction",clasificacion="PG-13"),
                 peliculas(id=94,marca= "disney", genero= "fantasía", año=2018, titulo="The Nutcracker and the Four Realms",clasificacion="PG"),
                 peliculas(id=95,marca= "20th century fox", genero= "animación", año= 2017, titulo="Ferdinand",clasificacion="PG"),
                 peliculas(id=96,marca= "lionsgate", genero= "musical", año= 2016, titulo="Hustle & Flow",clasificacion="R"),
                 peliculas(id=97,marca= "dreamworks", genero= "romance", año= 2015, titulo="The Light Between Oceans",clasificacion="PG-13"),
                 peliculas(id=98,marca= "columbia pictures", genero= "suspense", año= 2020, titulo="The Invisible Man",clasificacion="R"),
                 peliculas(id=99,marca= "universal", genero= "acción", año= 2019, titulo="Fast & Furious Presents: Hobbs & Shaw",clasificacion="PG-13"),
                 peliculas(id=100,marca= "sony", genero= "ciencia ficción", año= 2018, titulo="Venom",clasificacion="PG-13"),
                 peliculas(id=101,marca= "warner bros", genero= "comedia", año= 2017, titulo="The Lego Batman Movie",clasificacion="PG"),
                 peliculas(id=102,marca= "paramount", genero= "drama", año= 2016, titulo="Fences",clasificacion="PG-13"),
                 peliculas(id=103,marca="disney", genero= "aventura", año= 2015, titulo="Star Wars:Episode VII",clasificacion="PG-13"),
                 peliculas(id=104,marca= "20th century fox", genero= "fantasía", año= 2010, titulo="Percy Jackson & the Olympians: The Lightning Thief",clasificacion="PG"),
                 peliculas(id=105,marca= "lionsgate", genero= "animación", año= 2019, titulo="Wonder Park",clasificacion="PG"),
                 peliculas(id=106,marca= "dreamworks", genero= "musical", año= 2018, titulo="Trolls World Tour",clasificacion="PG"),
                 peliculas(id=107,marca= "columbia pictures", genero= "romance", año= 2017, titulo= "",clasificacion="PG-13"),
                 peliculas(id=108,marca= "universal", genero= "suspense", año=2016, titulo="Passengers",clasificacion="R"),
                 peliculas(id=109,marca= "sony", genero= "acción", año= 2015, titulo="The Girl on the Train",clasificacion=""),
                 peliculas(id=110,marca= "warner bros", genero= "ciencia ficción", año= 2020, titulo="Ad Astra",clasificacion="PG-13"),
                 peliculas(id=111,marca= "paramount", genero= "comedia", año= 2019, titulo="Booksmart",clasificacion="R"),
                 peliculas(id=112,marca= "disney", genero= "drama", año= 2010, titulo="Secretariat",clasificacion="PG"),
                 peliculas(id=113,marca= "20th century fox", genero= "aventura", año= 2017, titulo="Logan",clasificacion="R"),
                 peliculas(id=114,marca= "lionsgate", genero= "fantasía", año= 2016, titulo="Now You See Me 2",clasificacion="PG-13"),
                 peliculas(id=115,marca= "dreamworks", genero= "animación", año= 2013, titulo="Los Croods",clasificacion="PG"),
                 peliculas(id=116,marca= "columbia pictures", genero= "musical", año= 2005, titulo="Rent",clasificacion="PG-13"),
                 peliculas(id=117,marca= "universal", genero= "romance", año= 2019, titulo="Yesterday",clasificacion="PG-13"),
                 peliculas(id=118,marca= "sony", genero= "suspense", año= 2018, titulo="The Girl in the Spiders Web",clasificacion="R"),
                 peliculas(id=119,marca= "warner bros", genero="acción", año=2017, titulo="Wonder Woman",clasificacion="PG-13"),
                 peliculas(id=120,marca= "paramount", genero= "ciencia ficción", año= 2016, titulo="Terminator Genisys",clasificacion="PG-13"),
                 peliculas(id=121,marca= "disney", genero= "comedia", año= 2012, titulo= "Wreck It-Ralph",clasificacion="PG"),
                 peliculas(id=122,marca= "20th century fox", genero= "drama", año= 2020, titulo="The Descendants",clasificacion="R"),
                 peliculas(id=123,marca= "lionsgate", genero= "Animacion", año= 2008, titulo="Happily Never After",clasificacion="PG"),
                 peliculas(id=124,marca= "dreamworks", genero= "fantasía", año= 2013, titulo="Kun Fu Panda",clasificacion="PG"),
                 peliculas(id=125,marca= "columbia pictures", genero= "animación", año= 2017, titulo="Emoji",clasificacion="PG"),
                 peliculas(id=126,marca= "universal", genero= "musical", año= 2015, titulo="Straigth Outta Compton",clasificacion="R"),
                 peliculas(id=127,marca= "sony", genero= "romance", año= 2015, titulo="Aloha",clasificacion="PG-13"),
                 peliculas(id=128,marca= "warner bros", genero= "suspense", año= 2020, titulo="Tenet",clasificacion="PG-13"),
                 peliculas(id=129,marca= "paramount", genero= "acción", año= 2019, titulo="Terminator: Dark Fate",clasificacion="R"),
                 peliculas(id=130,marca= "disney", genero= "ciencia ficción", año= 2018, titulo="A Wrinkle in Time",clasificacion="PG"),
                 peliculas(id=131,marca= "20th century fox", genero="comedia", año= 2017, titulo="Diary of a Wimpy Kid",clasificacion="PG"),
                 peliculas(id=132,marca= "lionsgate", genero= "drama", año= 2016, titulo="Midnigth Sun",clasificacion="PG-13"),
                 peliculas(id=133,marca= "dreamworks", genero= "aventura", año= 2017, titulo="Captian Underpants",clasificacion="PG"),
                 peliculas(id=135,marca= "columbia pictures", genero= "fantasía", año= 2020, titulo="The Craft:Legacy",clasificacion="PG-13"),
                 peliculas(id=136,marca= "universal", genero= "animación", año= 2019, titulo="Abominable",clasificacion="PG"),
                 peliculas(id=137,marca= "sony", genero= "musical", año= 2009, titulo="This It Is",clasificacion="PG"),
                 peliculas(id=138,marca= "warner bros", genero= "romance", año= 2017, titulo="Everything  Everything",clasificacion="PG-13"),
                 peliculas(id=139,marca= "paramount", genero= "suspense", año= 2016, titulo="10 Cloverfield Lane",clasificacion="PG-13"),
                 peliculas(id=140,marca= "disney", genero= "acción", año= 2015, titulo="Tomorrowlan",clasificacion="PG"),
                 peliculas(id=141,marca= "20th century fox", genero= "ciencia ficción", año= 2020, titulo="The New Mutants",clasificacion="PG-13"),
                 peliculas(id=142,marca= "lionsgate", genero= "comedia", año= 2019, titulo="Long Shot",clasificacion="R"),
                 peliculas(id=143,marca= "dreamworks", genero= "drama", año= 2018, titulo="Green Book",clasificacion="PG-13"),
                 peliculas(id=144,marca= "columbia pictures", genero= "aventura", año= 2014, titulo="The Amazing Spider-Man 2",clasificacion="PG-13"),
                 peliculas(id=145,marca= "universal", genero= "fantasía", año= 2016, titulo="The Huntsman: Winters War",clasificacion="PG-13"),
                 peliculas(id=146,marca= "sony", genero= "animación", año= 2015, titulo="Hotel Transylvana",clasificacion="PG"),
                 peliculas(id=147,marca= "warner bros", genero= "musical", año= 2020, titulo="In The Heigths",clasificacion="PG-13"), 
                 peliculas(id=148,marca= "paramount", genero= "romance", año= 2017, titulo="Suburbircon",clasificacion="R"),
                 peliculas(id=149,marca= "disney", genero= "suspense", año= 2018, titulo="Bad Times at The El Royale",clasificacion="R"),
                 peliculas(id=150,marca= "20th century fox", genero= "acción", año= 2017, titulo="War For The Planet of the Apes",clasificacion="PG-13"),
                 peliculas(id=151,marca= "lionsgate", genero= "ciencia ficción", año= 2016, titulo="Vivarium",clasificacion="R"),
                 peliculas(id=152,marca= "dreamworks", genero= "comedia", año= 2012, titulo="Madadascar 3",clasificacion="PG"),
                 peliculas(id=153,marca= "columbia pictures", genero= "drama", año= 2020, titulo="Greyhound",clasificacion="PG-13"),
                 peliculas(id=154,marca= "universal", genero= "aventura", año= 2020, titulo="The Call of the Wild",clasificacion="PG"),
                 peliculas(id=155,marca= "sony", genero= "fantasía", año= 2018, titulo="The House With a CLock in Its Walls",clasificacion="PG"),
                 peliculas(id=156,marca= "warner bros", genero= "animación", año= 2019, titulo="The Lego Movie 2",clasificacion="PG"),
                 peliculas(id=157,marca= "paramount", genero= "musical", año= 2016, titulo="Florence Foster Jenkins",clasificacion="PG-13"),
                 peliculas(id=158,marca= "disney", genero= "romance", año= 2015, titulo="Cenicienta",clasificacion="PG"),
                 peliculas(id=159,marca= "20th century fox", genero= "suspense", año= 2006, titulo="Inside Man",clasificacion="R"),
                 peliculas(id=160,marca= "lionsgate", genero="acción", año= 2019, titulo="John Wick:Chapter 3",clasificacion="R"),
                 peliculas(id=161,marca= "dreamworks", genero="ciencia ficción", año=2015, titulo="Chappie",clasificacion="R"),
                 peliculas(id=162,marca= "columbia pictures", genero= "comedia", año= 2019, titulo="Once Upon an Time in Hollywood",clasificacion="R"),
                 peliculas(id=163,marca= "universal", genero= "drama", año= 2016, titulo="Manchester by the Sea",clasificacion="R"),
                 peliculas(id=164,marca= "sony", genero= "aventura", año= 2015, titulo="The Walk",clasificacion="PG"),
                 peliculas(id=165,marca= "warner bros", genero= "fantasía", año= 2013, titulo="The Hobbit",clasificacion="PG-13"),
                 peliculas(id=166,marca= "paramount", genero= "animación", año= 2011, titulo="Rango",clasificacion="PG"),
                 peliculas(id=167,marca= "disney", genero= "musical", año= 2007, titulo="Encantada",clasificacion="PG"),
                 peliculas(id=168,marca= "20th century fox", genero= "romance", año= 2006, titulo="The Devil Wears Prada",clasificacion="PG-13"),
                 peliculas(id=169,marca= "lionsgate", genero= "suspense", año= 2010, titulo="The Next Three Days",clasificacion="PG-13"),
                 peliculas(id=170,marca= "dreamworks", genero= "acción", año= 2016, titulo="Deepwater Horizon",clasificacion="PG-13"),
                 peliculas(id=171,marca= "columbia pictures", genero= "ciencia ficción", año= 2017, titulo="Life",clasificacion="R"),
                 peliculas(id=172,marca= "universal", genero= "comedia", año= 2012, titulo="Ted",clasificacion="R"),
                 peliculas(id=173,marca= "sony", genero= "drama", año= 2018, titulo="The Wife" ,clasificacion="R"),
                 peliculas(id=174,marca= "warner bros", genero= "aventura", año= 2019, titulo="Pokemon Detective Picachu",clasificacion="PG"),
                 peliculas(id=175,marca= "paramount", genero= "fantasía", año= 2016, titulo="Monster Trucks",clasificacion="PG"),
                 peliculas(id=176,marca= "disney", genero= "animación", año= 2019, titulo="Frozen II",clasificacion="PG"),
                 peliculas(id=177,marca= "universal", genero= "acción", año= 2015, titulo="Rapido Y Furiosos 7",clasificacion="PG-13"),
                 peliculas(id=178,marca= "paramount", genero= "ciencia ficción", año= 2018, titulo="A Quiet Place",clasificacion="PG-13"),
                 peliculas(id=179,marca= "warner bros", genero= "comedia", año= 2011, titulo="The Hangover Part II",clasificacion="R"),
                 peliculas(id=180,marca= "disney", genero= "drama", año= 2019, titulo="El Rey Leon",clasificacion="PG"),
                 peliculas(id=181,marca= "20th century fox", genero= "aventura", año= 2013, titulo="The Secret Life of Walter Milly",clasificacion="PG"),
                 peliculas(id=182,marca= "sony", genero= "fantasía", año= 2020, titulo="The Green Knigth",clasificacion="R"),
                 peliculas(id=183,marca= "lionsgate", genero= "animación", año= 2010, titulo="Alpha and Omega",clasificacion="PG"),
                 peliculas(id=184,marca= "dreamworks", genero= "musical", año= 2005, titulo="Madadascar",clasificacion="PG"),
                 peliculas(id=185,marca= "columbia pictures", genero= "romance", año= 2011, titulo="Crazy Stupid Love" ,clasificacion="PG-13"),
                 peliculas(id=186,marca= "universal", genero= "suspense", año= 2009, titulo="Duplicity",clasificacion="PG-13"),
                 peliculas(id=187,marca= "paramount", genero= "acción", año= 2012, titulo="Gi Joe Retalation",clasificacion="PG-13"),
                 peliculas(id=188,marca= "warner bros", genero= "ciencia ficción", año= 2014, titulo="Interstellar",clasificacion="PG-13"),
                 peliculas(id=189,marca= "disney", genero= "comedia", año= 2017, titulo="Cars 3",clasificacion="PG"),
                 peliculas(id=190,marca= "20th century fox", genero= "drama", año= 2012, titulo="Life Of Pi",clasificacion="PG"),
                 peliculas(id=191,marca= "sony", genero= "aventura", año= 2020, titulo="Jumanji:The Next Level",clasificacion="PG-13"),
                 peliculas(id=192,marca= "lionsgate", genero= "fantasía", año= 2010, titulo="The Last Airbender",clasificacion="PG"),
                 peliculas(id=193,marca= "dreamworks", genero= "animación", año= 2007, titulo="Bee Movie",clasificacion="PG"),
                 peliculas(id=194,marca= "columbia pictures", genero= "musical", año= 2012, titulo="Les Miserables",clasificacion="PG-13"),
                 peliculas(id=195,marca= "universal", genero= "romance", año= 2013, titulo="About Time",clasificacion="R"),
                 peliculas(id=196,marca= "paramount", genero= "suspense", año= 2018, titulo="Flight",clasificacion="R"),
                 peliculas(id=197,marca= "warner bros", genero= "acción", año= 2010, titulo="Inception",clasificacion="PG-13"),
                 peliculas(id=198,marca= "disney", genero= "ciencia ficción", año= 2014, titulo="Guardians of the Galaxy",clasificacion="PG-13"),
                 peliculas(id=199,marca= "20th century fox", genero= "comedia", año= 2015, titulo="Spy",clasificacion="R"),
                 peliculas(id=200,marca= "sony", genero= "drama", año= 2021, titulo="The Father",clasificacion="PG-13")]

@app.get("/peliculas")
async def imprimir():
    return peliculas_list

@app.get("/peliculasclass/")
async def peliculasclass(id:int):
    peliculas = filter (lambda peliculas: peliculas.id == id, peliculas_list)
    try:
        return list(peliculas)[0]
    except:
        return{"error":"No se ha encontrado la pelicula que buscas"} #http://127.0.0.1:8000/peliculasclass/?id=1
    
@app.get("/peliculasclass2/")
async def peliculasclass(marca:str, genero:str):
    peliculas=filter (lambda peliculas: peliculas.marca == marca, peliculas_list)#Función de orden superior
    peliculas1=filter (lambda peliculas: peliculas.genero == genero, peliculas)#Función de orden superior
    try:
        return list(peliculas1) #se borra el [0] para que se muestren todas las peliculas que coincidan con los filtros
    except:
        return{"error":"No se ha encontrado la pelicula"} #http://127.0.0.1:8000/peliculasclass2/?marca=sony&genero=drama
    
@app.get("/peliculasclass3/")
async def peliculaclass(marca:str, genero:str, año:int):
    peliculas=filter (lambda peliculas: peliculas.marca == marca, peliculas_list)#Función de orden superior
    peliculas1=filter (lambda peliculas: peliculas.genero == genero, peliculas)#Función de orden superior
    peliculas2=filter (lambda peliculas: peliculas.año == año, peliculas1)
    try:
        return list(peliculas2) #se borra el [0] para que se muestren todas las peliculas que coincidan con los filtros
    except:
        return{"error":"No se ha encontrado la pelicula"} #http://127.0.0.1:8000/peliculasclass3/?marca=sony&genero=drama&año=2015
    
@app.get("/peliculasclass4/")
async def peliculasclass(marca:str, genero:str, año:int, titulo:str):
    peliculas=filter (lambda peliculas: peliculas.marca == marca, peliculas_list)#Función de orden superior
    peliculas1=filter (lambda peliculas: peliculas.genero == genero, peliculas)#Función de orden superior
    peliculas2=filter (lambda peliculas: peliculas.año == año, peliculas1)
    peliculas3=filter (lambda peliculas: peliculas.titulo == titulo, peliculas2)
    try:
        return list(peliculas3) #se borra el [0] para que se muestren todas las peliculas que coincidan con los filtros
    except:
        return{"error":"No se ha encontrado la pelicula"} #http://127.0.0.1:8000/peliculasclass4/?marca=sony&genero=drama&año=2018&titulo=The Wife
    
    
@app.get("/peliculasclass5/")
async def peliculasclass(marca:str, genero:str, año:int, titulo:str, clasificacion:str):
    peliculas=filter (lambda peliculas: peliculas.marca == marca, peliculas_list)#Función de orden superior
    peliculas1=filter (lambda peliculas: peliculas.genero == genero, peliculas)#Función de orden superior
    peliculas2=filter (lambda peliculas: peliculas.año == año, peliculas1)
    peliculas3=filter (lambda peliculas: peliculas.titulo == titulo, peliculas2)
    peliculas4=filter (lambda peliculas: peliculas.clasificacion == clasificacion, peliculas3)
    try:
        return list(peliculas4) #se borra el [0] para que se muestren todas las peliculas que coincidan con los filtros
    except:
        return{"error":"No se ha encontrado la pelicula"}  #http://127.0.0.1:8000/peliculasclass5/?marca=sony&genero=drama&año=2018&titulo=The Wife&clasificacion=R
    
    
