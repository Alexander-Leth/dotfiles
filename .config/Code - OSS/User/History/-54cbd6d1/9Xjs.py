from typing import List
from sqlalchemy.orm import Session
from exceptions import EntityInfoInfoAlreadyExistError, EntityInfoNotFoundError
from models import EntityInfo
from schemas import CreateAndUpdateEntity


# Function to get list of entity info
def get_all_entities(session: Session, limit: int, offset: int) -> List[EntityInfo]:
    return session.query(EntityInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular entity
def get_entity_info_by_id(session: Session, _id: int) -> EntityInfo:
    entity_info = session.query(EntityInfo).get(_id)

    if entity_info is None:
        raise EntityInfoNotFoundError

    return entity_info


# Function to add a new entity info to the database
def create_entity(session: Session, entity_info: CreateAndUpdateEntity) -> EntityInfo:
    entity_details = session.query(EntityInfo).filter(EntityInfo.manufacturer == entity_info.manufacturer, EntityInfo.modelName == entity_info.modelName).first()
    if entity_details is not None:
        raise EntityInfoInfoAlreadyExistError

    new_entity_info = CarInfo(**entity_info.dict())
    session.add(new_entity_info)
    session.commit()
    session.refresh(new_entity_info)
    return new_entity_info


# Function to update details of the enitity
def update_entity_info(session: Session, _id: int, info_update: CreateAndUpdateEntity) -> EntityInfo:
    entity_info = get_entity_info_by_id(session, _id)

    if entity_info is None:
        raise EntityInfoNotFoundError

    entity_info.name = info_update.name
    entity_info.energyValue = info_update.energyValue
    entity_info.Duration = info_update.Duration
    entity_info.priority = info_update.priority
    entity_info.taskFun = info_update.taskFun
    entity_info.entityType = info_update.entityType

    session.commit()
    session.refresh(entity_info)

    return entity_info


# Function to delete a entity info from the db
def delete_car_info(session: Session, _id: int):
    entity_info = get_entity_info_by_id(session, _id)

    if entity_info is None:
        raise EntityInfoNotFoundError

    session.delete(entity_info)
    session.commit()

    return
