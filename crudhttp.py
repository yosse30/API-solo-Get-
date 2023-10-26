from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app= FastAPI()

class Passenger(BaseModel):
    id: int
    Name: str
    Pclass: int
    Survived: int
    Sex: str
    Age: int
    SibSp: int
    Parch: int
    Ticket: int


passenger_list=[Passenger(id= 1, Name= "Arnold-Franchi, Mrs. Josef (Josefine Franchi)", Pclass= 3 , Survived= 0, Sex= "female" , Age= 10, SibSp= 1 , Parch= 0, Ticket= 349237), 
                Passenger(id= 2,Name= "Panula, Master. Juha Niilo", Pclass= 3 , Survived= 0, Sex= "male" , Age= 7, SibSp= 4 , Parch=1 , Ticket= 3101295), 
                Passenger(id= 3, Name= "Nosworthy, Mr. Richard Cater	", Pclass= 3 , Survived= 0, Sex= "male" , Age= 21, SibSp= 0 , Parch= 0, Ticket= 439886),
                Passenger(id= 4, Name= "Harper, Mrs. Henry Sleeper (Myna Haxtun)", Pclass= 1 , Survived= 1, Sex= "female" , Age= 49, SibSp= 1 , Parch= 0, Ticket= 17572),
                Passenger(id= 5, Name= "Faunthorpe, Mrs. Lizzie (Elizabeth Anne Wilkinson)", Pclass= 2 , Survived= 1, Sex= "female" , Age= 29, SibSp= 1 , Parch= 0, Ticket= 2926), 
                Passenger(id= 6, Name= "Ostby, Mr. Engelhart Cornelius", Pclass= 1 , Survived= 0, Sex= "male" , Age= 65, SibSp= 0 , Parch= 1, Ticket= 113509),
                Passenger(id= 7, Name= "Woolner, Mr. Hugh", Pclass= 1 , Survived= 1, Sex= "male" , Age= 0, SibSp= 0 , Parch= 0, Ticket= 19947), 
                Passenger(id= 8, Name= "Rugg, Miss. Emily", Pclass= 2 , Survived= 1, Sex= "female" , Age= 21, SibSp= 0 , Parch= 0, Ticket=31026),
                Passenger(id= 9, Name= "Novel, Mr. Mansouer", Pclass= 3 , Survived= 0, Sex= "male" , Age= 285, SibSp= 0 , Parch= 0, Ticket= 2697), 
                Passenger(id= 10, Name= "West, Miss. Constance Mirium", Pclass= 2 , Survived= 1, Sex= "female" , Age= 5, SibSp= 1 , Parch= 2, Ticket=34651),
                Passenger(id= 11, Name="Goodwin, Master. William Frederick", Pclass= 3 , Survived= 0, Sex= "male" , Age= 11, SibSp= 5 , Parch= 2, Ticket= 2144), 
                Passenger(id= 12, Name= "Sirayanian, Mr. Orsen", Pclass= 3 , Survived= 0, Sex= "male" , Age= 22, SibSp= 0 , Parch= 0, Ticket= 2669),
                Passenger(id= 13, Name= "Icard, Miss. Amelie", Pclass= 1 , Survived= 1, Sex= "female" , Age= 38, SibSp= 0 , Parch= 0, Ticket= 113572), 
                Passenger(id= 14, Name= "Harris, Mr. Henry Birkhardt", Pclass= 1 , Survived= 0, Sex= "male" , Age= 45, SibSp= 1 , Parch= 0, Ticket= 36973),
                Passenger(id= 15, Name= "Skoog, Master. Harald", Pclass= 3 , Survived= 0, Sex= "male" , Age= 4, SibSp= 3 , Parch= 2, Ticket= 347088), 
                Passenger(id= 16, Name="Stewart, Mr. Albert A", Pclass= 1 , Survived= 0, Sex= "male" , Age=0 , SibSp= 0 , Parch= 0, Ticket=17605),
                Passenger(id= 17, Name= "Moubarek, Master. Gerios", Pclass= 3 , Survived= 1, Sex= "male" , Age= 0, SibSp= 1 , Parch= 1, Ticket= 2661), 
                Passenger(id= 18, Name= "Nye, Mrs. (Elizabeth Ramell)", Pclass= 2 , Survived= 1, Sex= "female" , Age= 29, SibSp= 0 , Parch= 0, Ticket=29395), 
                Passenger(id= 19, Name= "Crease, Mr. Ernest James", Pclass= 3 , Survived= 0, Sex= "male" , Age= 19, SibSp= 0 , Parch= 0, Ticket=3464), 
                Passenger(id= 20, Name= "Andersson, Miss. Erna Alexandra", Pclass= 3 , Survived= 1, Sex= "female" , Age= 17, SibSp= 4 , Parch= 2, Ticket= 3101281), 
                Passenger(id= 21, Name= "Kink, Mr. Vincenz", Pclass= 3 , Survived= 0, Sex= "male" , Age= 26, SibSp= 2 , Parch= 0, Ticket= 315151), 
                Passenger(id= 22, Name= "Jenkin, Mr. Stephen Curnow", Pclass= 2 , Survived= 0, Sex= "male" , Age= 32, SibSp= 0 , Parch= 0, Ticket=33111), 
                Passenger(id= 23, Name= "Goodwin, Miss. Lillian Amy", Pclass= 3 , Survived= 0, Sex= "female" , Age= 16, SibSp= 5 , Parch= 2, Ticket= 2144), 
                Passenger(id=24,  Name= "Hood, Mr. Ambrose Jr", Pclass= 2 , Survived= 0, Sex= "male" , Age= 21, SibSp= 0 , Parch= 0, Ticket=14879), 
                Passenger(id= 25, Name= "Chronopoulos, Mr. Apostolos", Pclass= 3 , Survived= 0, Sex= "male" , Age= 26, SibSp= 1 , Parch= 0, Ticket= 2680)]

@app.get("/passenger/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def passenger():
    return (passenger_list)

@app.post("/passenger/", response_model=Passenger, status_code=status.HTTP_201_CREATED, response_description="El pasajero se añadió correctamente")
async def create_passenger(passenger: Passenger):
    for saved_passenger in passenger_list:
        if saved_passenger.id == passenger.id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El pasajero ya existe")
    passenger_list.append(passenger)
    return passenger

@app.put("/passenger/", response_model=Passenger, status_code=status.HTTP_202_ACCEPTED, response_description="La información del pasajero se actualizó correctamente")
async def update_passenger(passenger: Passenger):
    found = False
    for index, saved_passenger in enumerate(passenger_list):
        if saved_passenger.id == passenger.id:
            passenger_list[index] = passenger
            found = True

    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontró el pasajero con el ID proporcionado")
    return passenger, {"respuesta": "El pasajero se ha actualizado exitosamente!"}
    
@app.delete("/passenger/{id}", status_code=status.HTTP_202_ACCEPTED, response_description= "El pasajero se elimino correctamente")
async def passengerclass(id: int):
    global passenger_list

    updated_passenger_list = [passenger for passenger in passenger_list if passenger.id != id]

    if len(updated_passenger_list) == len(passenger_list):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró el pasajero con el ID proporcionado")
    else:
        passenger_list = updated_passenger_list
        return {"message": "El pasajero se ha eliminado exitosamente"}