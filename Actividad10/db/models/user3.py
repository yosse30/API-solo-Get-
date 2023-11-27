from pydantic  import BaseModel


class User (BaseModel):
    id: str | None
    marca:str
    genero:str
    año:str
    titulo: str