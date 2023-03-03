#These tables hold the data which the mod-algorithm will use to adjust the 
#bundle algorithm and the energy values

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String, Integer, Enum, ForeignKey
from database import Base
from . import data_modules
from . import comp_modules

import enum

class ModEntity(Base):
    __tablename__ = 'mod_entity'

    id: Mapped [int] = mapped_column(Integer, primary_key=True)
    exposureCoeficent: Mapped [int] = mapped_column(Integer)
    feedbackCoeficient: Mapped [int] = mapped_column(Integer)
    entity_id: Mapped [int] = mapped_column(Integer, ForeignKey('entity.id'))

class ModBundle(Base):
    __tablename__ = 'mod_bundle'

    id: Mapped [int] = mapped_column(Integer, primary_key=True)
    ratioCoeficent: Mapped [int] = mapped_column(Integer)
    feedbackCoeficient: Mapped [int] = mapped_column(Integer)
    bundle_id: Mapped [int] = mapped_column(Integer, ForeignKey('bundle.id'))

class ModDay(Base):
    __tablename__ = 'mod_day'
    id: Mapped [int] = mapped_column(Integer, primary_key=True)
    exposureCoeficent: Mapped [int] = mapped_column(Integer)
    deviationCoeficient: Mapped [int] = mapped_column(Integer)
    sleepCoeficent: Mapped [int] = mapped_column(Integer)
    seasonCoeficient: Mapped [int] = mapped_column(Integer)
    day_id: Mapped [int] = mapped_column(Integer, ForeignKey('day.id'))