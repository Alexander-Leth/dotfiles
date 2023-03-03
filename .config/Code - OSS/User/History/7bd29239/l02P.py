# This module contains the root data which makes up the comps and the mods

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String, Integer, Enum, Boolean, ForeignKey
from database import Base

import enum

class EntityType(str, enum.Enum):
    task = "task"
    pause = "pause"

class EntityCategory(str, enum.Enum):
    cooking = "cooking"
    cleaning = "cleaning"


class EntityData(Base):
    __tablename__ = "entity"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    energyValue: Mapped[int] = mapped_column(Integer)
    energWeight = relationship('ModData', backref='entity')
    Duration = Mapped(Integer)
    priority: Mapped[int] = mapped_column(Integer)
    taskFun: Mapped[bool] = mapped_column(Boolean)
    entityType: Mapped[str] = mapped_column(Enum(EntityType)) 
    category: Mapped[str] = mapped_column(Enum(EntityCategory))
    recipe = relationship('Recipe', backref='entity')
    bundle_id: Mapped[int] = mapped_column(Integer, ForeignKey('bundle.id'))

class RecipieData(Base):
    __tablename__ = 'recipe'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    ingredients: Mapped[str] = mapped_column(String)
    instructions: Mapped[str] = mapped_column(String)
    entity_id: Mapped[int] = mapped_column(Integer, ForeignKey('entity.id'))    

class SleepData(Base):
    __tablename__ = 'sleep'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[int] = mapped_column(Integer)
    timeSlept: Mapped[int] = mapped_column(Integer)
    deepSleep: Mapped[int] = mapped_column(Integer)
    REMSleep: Mapped[int] = mapped_column(Integer)
    consistency: Mapped[int] = mapped_column(Integer)
    wakeCount: Mapped[int] = mapped_column(Integer) 

class MorningData(Base):
    __tablename__ = 'morning'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    ingredients: Mapped[str] = mapped_column(String)
    instructions: Mapped[str] = mapped_column(String)
    entity_id: Mapped[int] = mapped_column(Integer, ForeignKey('entity.id'))

class EveningData(Base):
    __tablename__ = 'evening'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    ingredients: Mapped[str] = mapped_column(String)
    instructions: Mapped[str] = mapped_column(String)
    entity_id: Mapped[int] = mapped_column(Integer, ForeignKey('entity.id'))

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




