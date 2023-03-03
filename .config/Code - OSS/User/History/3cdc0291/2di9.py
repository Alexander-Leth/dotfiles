from typing import List
from sqlalchemy.orm import Session
from exceptions import EntityDataAlreadyExistError, EntityDataNotFoundError
from models.data_modules import EntityData
from schemas import CreateAndUpdateEntity
from . import models, schemas

class CrudEntity

    #gets passed the entity_id and returns said entity
    def get_entity(db: Session, entity_id: int):
        return db.query(models.EntityData).filter(models.EntityData.id == entity_id).first()

    #returns all enties
    def get_entites(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    #returns a new entity
    def create_entity(db: Session, entity_data: schemas.CreateAndUpdateEntity) -> EntityData:
        db_entity = session.query(EntityData).filter(EntityData.name == db_entity.name, 
        EntityData.energyValue == db_entity.energyValue, 
        EntityData.Duration == db_entity.Duration,
        EntityData.isFun == db_entity.isFun,
        EntityData.priority == db_entity.priority
        EntityData.entityType == db_entity.entityType,
        EntityData.category == db_entity.category).first()
        return db_user

