from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, ForeignKey
from database import Base
import enum


class EntityType(str, enum.Enum):
    task = "task"
    pause = "pause"

class TaskFun(bool, enum.Enum):
    notFun = False
    fun = True

class EntityData(Base):
    __tablename__ = "entity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    energyValue = Column(Integer)
    energWeight = relationship('ModData', backref='entity')
    Duration = Column(Integer)
    priority = Column(Integer)
    taskFun = Column(Enum(TaskFun))
    entityType = Column(Enum(EntityType)) 
    category = Column(String)
    recipe = relationship('Recipe', backref='entity')
    bundle_id = Column(Integer, ForeignKey('bundle.id'))

class RecipieData(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    instructions = Column(String)
    entity_id = Column(Integer, ForeignKey('entity.id'))

class SleepData(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    instructions = Column(String)
    entity_id = Column(Integer, ForeignKey('entity.id'))

class MorningData(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    instructions = Column(String)
    entity_id = Column(Integer, ForeignKey('entity.id'))

class EveningData(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    instructions = Column(String)
    entity_id = Column(Integer, ForeignKey('entity.id'))

create table entity (
id int AUTO_INCREMENT PRIMARY KEY, 
name varchar(30) NOT NULL, 
energyValue varchar int NOT NULL,
Duration int NOT NULL, 
priority int NOT NULL, 
taskfun enum (False, True) NOT NULL, 
entityType enum ('task', 'pause') NOT NULL,
category varchar(30) NOT NULL,
recipe relationship
);

create table recipie (
id int AUTO_INCEMENT PRIMARY KEY,
name varchar(30) NOT NULL,
ingredients varchar(255) NOT NULL,
instructions varchar(255) NOT NULL,
task_id relationship NOT NULL
);




