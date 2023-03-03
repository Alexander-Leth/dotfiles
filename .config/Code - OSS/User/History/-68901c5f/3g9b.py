from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_all_entities, create_entity, get_entity_info_by_id, update_entity_info, delete_entity_info
from database import get_db
from exceptions import EntityInfoException
from schemas import Entity, CreateAndUpdateEntity, PaginatedEntityInfo

router = APIRouter()

@cbv(router)
class Entities:
    db: Session = Depends(get_db)

    @router.get("/entites", response_model=PaginatedEntityInfo)
    def list_entites(self, limit: int = 10, offset: int = 0):

        entity_list = get_all_entities(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": cars_list}

        return response

    # API endpoint to add an entity info to the database
    @router.post("/entites")
    def add_entity(self, entity_info: CreateAndUpdateEntity):

        try:
            entity_info = create_car(self.session, entity_info)
            return entity_info
        except EntityInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular entity 
@router.get("/entites/{entity_id}", response_model=Entity)
def get_entity_info(entity_id: int, session: Session = Depends(get_db)):

    try:
        entity_info = get_entity_info_by_id(session, entity_id)
        return entity_info
    except EntityInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update an existing entity info
@router.put("/entites/{entity_id}", response_model=Entity)
def update_entity(entity_id: int, new_info: CreateAndUpdateEntity, session: Session = Depends(get_db)):

    try:
        entity_info = update_entity_info(session, entity_id, new_info)
        return entity_info
    except EntityInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete an entity info from the data base
@router.delete("/entites/{entity_id}")
def delete_car(entity_id: int, session: Session = Depends(get_db)):

    try:
        return delete_car_info(session, entity_id)
    except EntitesInfoException as cie:
        raise HTTPException(**cie.__dict__)
