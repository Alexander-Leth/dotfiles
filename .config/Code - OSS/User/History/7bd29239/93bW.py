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
    project = "project"
    workout = "workout"
    practice = "practice"
    work = "work"
    school = "school"
    friends_and_family = "friends and family"



class UserGender(str, enum.Enum):
    male = "male"
    female = "female"

class UserData(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    age: Mapped[str] = mapped_column(String(255))
    gender: Mapped[str] = mapped_column(Enum(UserGender)))
    country: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(String(255))
    email: mapped[str] = mapped_column(String(225))
    password: Mapped[str] = mapped_column(String(255))
    
    
1
class EntityData(Base):
    __tablename__ = "entity"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    energyValue: Mapped[int] = mapped_column(Integer)
    Duration = Mapped(Integer)
    priority: Mapped[int] = mapped_column(Integer)
    entityType: Mapped[str] = mapped_column(Enum(EntityType)) 
    category: Mapped[str] = mapped_column(Enum(EntityCategory))
    bundle_id: Mapped[int] = mapped_column(Integer, ForeignKey('bundle.id'))

    recipe = relationship('Recipe', backref='entity')
    energWeight = relationship('ModData', backref='entity')

class RecipieData(Base):
    __tablename__ = 'recipe'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    ingredients: Mapped[str] = mapped_column(String(255))
    instructions: Mapped[str] = mapped_column(String(255))
    price: Mapped[int] = mapped_column(Integer)
    cook_time: Mapped[int] = mapped_column(Integer)
    entity_id: Mapped[int] = mapped_column(Integer, ForeignKey('entity.id'))    

class SleepData(Base):
    __tablename__ = 'sleep'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[int] = mapped_column(Integer)
    wentToBed: Mapped[int] = mapped_column(Integer)
    gotUp: Mapped[int] = mapped_column(Integer)
    deepSleep: Mapped[int] = mapped_column(Integer)
    REMSleep: Mapped[int] = mapped_column(Integer)
    wakeCount: Mapped[int] = mapped_column(Integer) 




