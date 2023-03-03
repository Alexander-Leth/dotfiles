from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, ForeignKey
from database import Base
from . import data_modules
from . import comp_modules
import enum

class ModEntity(Base):
    __tablename__ = 'mod_entity'

    id = Column(Integer, primary_key=True)
    exposureCoeficent = Column(Integer)
    feedbackCoeficient = Column(Integer)
    task_id = Column(Integer, ForeignKey('entity.id'))

class ModBundle(Base):
    __tablename__ = 'mod_bundle'

    id = Column(Integer, primary_key=True)
    ratioCoeficent = Column(Integer)
    feedbackCoeficient = Column(Integer)
    bundle_id = Column(Integer, ForeignKey('bundle.id'))

class ModDay(Base):
    __tablename__ = 'mod_day'
    pass