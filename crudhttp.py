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
    Ticket: str


passenger_list=[]

@app.get("/passenger/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def passenger():
    return (passenger_list)

@app.post("/passenger/", response_model=Passenger, status_code=status.HTTP_201_CREATED, response_description="El pasajero se añadio correctamente")
async def passengerclass(pasajeros:Passenger):
    found=False
    
    for index, saved_passenger in enumerate(passenger_list):
        if saved_passenger.id == passenger.id:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el pasajero ya existe")
    else:
        passenger_list.append(passenger)
        return passenger
    
@app.put("/passenger/", response_model=Passenger, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion del pasajero se actualizo correctamente")
async def passengerclass(passenger:Passenger):
    
    found=False

    for index, saved_passenger in enumerate(passenger_list):
        if saved_passenger.id == passenger.id:
            passenger_list[index] = passenger
            found=True
    
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró el pasajero con el ID proporcionado")
    else:
        return passenger, {"respuesta":"El pasajero se ha actualizado exitosamente!"}
    
@app.delete("/passenger/{id}", status_code=status.HTTP_202_ACCEPTED, response_description= "El pasajero se elimino correctamente")
async def passengerclass(id: int):
    global passenger_list

    updated_passenger_list = [passenger for passenger in passenger_list if passenger.id != id]

    if len(updated_passenger_list) == len(passenger_list):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró el pasajero con el ID proporcionado")
    else:
        passenger_list = updated_passenger_list
        return {"message": "El pasajero se ha eliminado exitosamente"}