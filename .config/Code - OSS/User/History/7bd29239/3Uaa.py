from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from database import Base
import enum


class EntityType(str, enum.Enum):
    task = "task"
    pause = "pause"

class TaskFun(bool, enum.Enum):
    notFun = False
    fun = True

class EntityInfo(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    energyValue = Column(Integer)
    Duration = Column(Integer)
    priority = Column(Integer)
    taskFun = Column(Enum(TaskFun))
    entityType = Column(Enum(EntityType))

create table car (
id int AUTO_INCREMENT PRIMARY KEY, 
name varchar(30) NOT NULL, 
energyValue varchar int NOT NULL,
Duration int NOT NULL, 
priority int NOT NULL, 
taskfun enum (False, True) NOT NULL, 
entityType enum ('task', 'pause') NOT NULL
);
