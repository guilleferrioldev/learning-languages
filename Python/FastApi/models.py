from enum import Enum
from datetime import date
from pydantic import BaseModel, validator
from sqlmodel import SQLModel, Field

class GenreURLChoices(Enum): 
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip_hop'

class GenreChoices(Enum): 
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip_hop'

class Album(BaseModel):
    title: str 
    released_date: date

class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Album] = []

class BandCreate(BandBase):
    @validator('genre', pre=True)
    def title_case_genre(cls, value):
        return value.title()

class BandWithId(BandBase):
    id: int
