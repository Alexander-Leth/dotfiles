from typing import List
from sqlalchemy.orm import Session
from exceptions import EntityDataAlreadyExistError, EntityDataNotFoundError
from models import EntityData
from schemas import CreateAndUpdateEntity


# Function to get list of entity info
def get_all_entities(session: Session, limit: int, offset: int) -> List[EntityData]:
    return session.query(EntityData).offset(offset).limit(limit).all()


# Function to  get info of a particular entity
def get_entity_info_by_id(session: Session, _id: int) -> EntityData:
    entity_data = session.query(EntityData).get(_id)

    if entity_info is None:
        raise EntityDataNotFoundError

    return entity_info


# Function to add a new entity info to the database
def create_entity(session: Session, entity_info: CreateAndUpdateEntity) -> EntityData:
    entity_details = session.query(EntityData).filter(EntityData.manufacturer == entity_info.manufacturer, EntityData.modelName == entity_info.modelName).first()
    if entity_details is not None:
        raise EntityInfoInfoAlreadyExistError

    new_entity_data = CarInfo(**entity_info.dict())
    session.add(new_entity_data)
    session.commit()
    session.refresh(new_entity_data)
    return new_entity_data


# Function to update details of the enitity
def update_entity_info(session: Session, _id: int, info_update: CreateAndUpdateEntity) -> EntityData:
    entity_info = get_entity_info_by_id(session, _id)

    if entity_info is None:
        raise EntityDataNotFoundError

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
def delete_entity_info(session: Session, _id: int):
    entity_info = get_entity_info_by_id(session, _id)

    if entity_info is None:
        raise EntityDataNotFoundError

    session.delete(entity_info)
    session.commit()

    return
