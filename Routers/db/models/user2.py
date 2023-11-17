from pydantic  import BaseModel


class User (BaseModel):
    id: str | None
    Name: str
    Pclass: int
    Survived: int
    Sex: str
    Age: int
    SibSp: int
    Parch: int
    Ticket: int
    