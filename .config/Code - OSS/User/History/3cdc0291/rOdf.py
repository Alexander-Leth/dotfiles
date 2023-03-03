from typing import List
from sqlalchemy.orm import Session
from exceptions import EntityDataAlreadyExistError, EntityDataNotFoundError
from models.data_models import EntityData, RecipieData
from schemas.data_schemas import CreateAndUpdateEntity
  
class CrudRecipe:
    
    #gets passed the user_id and returns said user
    def get_user(db: Session, user_id: int):
        return db.query(data_models.UserData).filter(data_models.UserData.id == user_id).first()

    def create_user(db: Session, user_data: schemas.CreateAndUpdateUser): -> UserData:
        db_user = session.query(UserData).filter(UserData.name == db_user.name,
        UserData.email == db_user.email,
        UserData.password == db_user.password,
        UserData.age == db_user.age,
        UserData.gender == db_user.gender,
        UserData.country == db_user.country,
        UserData.city == db_user.city).first()
        return db_user

class CrudRecipe:

    #gets passed the recipie_id and returns said recipe
    def get_recipie(db: Session, recipie_id: int):
        return db.query(models.RecipieData).filter(models.RecipieData.id == recipie_id).first()

    #returns all recipies
    def get_recipies(db: Session):
        return db.query(data_models.RecipieData).all()

    #returns a new recipe
    def create_recipie(db: Session, recipie_data: schemas.CreateAndUpdateRecipe): -> RecipieData:
        db_recipe = session.query(RecipieData).filter(RecipieData.name == db_recipie.name, 
        RecipieData.ingerdients == db_recipie.ingerdients, 
        RecipieData.instructions == db_recipie.instructions,
        RecipieData.price == db_recipie.price,
        RecipieData.cook_time == db_recipie.cook_time).first()
        return db_recipe


class CrudEntity:

    #gets passed the entity_id and returns said entity
    def get_entity(db: Session, entity_id: int):
        return db.query(models.EntityData).filter(models.EntityData.id == entity_id).first()

    #returns all enties
    def get_entites(db: Session):
        return db.query(data_models.EntityData).all()

    #returns a new entity
    def create_entity(db: Session, entity_data: schemas.CreateAndUpdateEntity): -> EntityData:
        db_entity = session.query(EntityData).filter(EntityData.name == db_entity.name, 
        EntityData.energyValue == db_entity.energyValue, 
        EntityData.Duration == db_entity.Duration,
        EntityData.isFun == db_entity.isFun,
        EntityData.priority == db_entity.priority
        EntityData.entityType == db_entity.entityType,
        EntityData.category == db_entity.category).first()
        return db_entity


    

