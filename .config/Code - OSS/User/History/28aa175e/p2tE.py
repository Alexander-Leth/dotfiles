#This module contains the sql tables of compilated entities 

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String, Integer, Enum, ForeignKey
from database import Base
from . import data_modules
from . import mod_modules

import enum

class Bundle(Base):
    __tablename__ = 'bundle'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    entity = relationship('Bundle', backref='bundle')
    size: Mapped[int] = mapped_column(integer)
    sizeWeight = relationship('Mod_bundle', backref='bundle')
    day_id: Mapped[int] = mapped_column(Integer, ForeignKey('day.id'))

class Day(Base):
    __tablename__ = 'day'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bundle = relationship('Day', backref='day')
    energyMax: Mapped[int] = mapped_column(Integer)
    date: Mapped[int] = mapped_column(Integer)
