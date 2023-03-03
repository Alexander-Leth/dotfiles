from pydantic import BaseModel
from models import EntityType
from typing import Optional, List


class CreateAndUpdateEntity(BaseModel):
    name: str
    energyValue: str
    Duration: int
    priority: int
    category: enum(Category)
    entityType: enum(EntityType)

    class Config:
        orm_mode = True

class CreateAndUpdateRecipie(BaseModel):
    name: str
    ingerdients: str
    cook_time: int
    instructions: int

    class Config:
        orm_mode = True

class CreateAndUpdateSleep(BaseModel):
    date: int
    wentToBed: str
    gotUp: int
    deepSleep: int
    REMSleep: int
    wakeCount: int

    class Config:
        orm_mode = True

class CreateAndUpdateUser(BaseModel):
    name: str
    password: str
    age: int
    gender: str
    country: str
    city: str

    class Config:
        orm_mode = True


