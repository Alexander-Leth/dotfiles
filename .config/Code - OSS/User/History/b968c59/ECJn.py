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

class CreateAndUpdateRecipie(BaseModel):
    name: str
    ingerdients: str
    cook_time: int
    instructions: int

class CreateAndUpdateSleep(BaseModel):
    date: int
    wentToBed: str
    gotUp: int
    deepSleep: int
    REMSleep: int
    wakeCount: int

class CreateAndUpdateUser(BaseModel):
    name: str
    password: str
    age: int
    gender: str
    country: str
    city: str


