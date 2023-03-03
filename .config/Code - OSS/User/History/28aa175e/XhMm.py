from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, ForeignKey
from database import Base
from . import data_modules
from . import mod_modules
import enum

class Bundle(Base):
    __tablename__ = 'bundle'

    id = Column(Integer, primary_key=True)
    entity = relationship('Bundle', backref='bundle')
    size = Column(integer)
    sizeWeight = relationship('Mod_bundle', backref='bundle')
    day_id = Column(Integer, ForeignKey('day.id'))

class Day(Base):
    __tablename__ = 'day'

    id = Column(Integer, primary_key=True)
    bundle = relationship('Day', backref='day')
    date = Column(integer)
