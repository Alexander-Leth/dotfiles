from pydantic import BaseModel
from models import FuelType
from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateEntity(BaseModel):
    name: str
    modelName: str
    cc: int
    onRoadPrice: int
    seatingCapacity: int
    gearBox: int
    fuelType: FuelType


# TO support list and get APIs
class Car(CreateAndUpdateEntity):
    id: int

    class Config:
        orm_mode = True


# To support list cars API
class PaginatedEntityInfo(BaseModel):
    limit: int
    offset: int
    data: List[Entity]
