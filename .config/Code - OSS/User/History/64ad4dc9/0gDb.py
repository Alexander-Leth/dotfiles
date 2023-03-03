from pydantic import BaseModel
from models import EntityType
from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateEntity(BaseModel):
    name: str
    energyValue: str
    Duration: int
    priority: int
    taskFun: TaskFun
    entityType: EntityType


# TO support list and get APIs
class Entity(CreateAndUpdateEntity):
    id: int

    class Config:
        orm_mode = True


# To support list enties API
class PaginatedEntityInfo(BaseModel):
    limit: int
    offset: int
    data: List[Entity]
