"""
Actions module for handling database operations related to trainers, pokemons, and items
"""
from sqlalchemy.orm import Session
from . import models, schemas
from .utils.pokeapi import battle_pokemon, get_pokemon_name, get_pokemon_stats_api


def get_trainer(database: Session, trainer_id: int):
    """
        Find a user by his id
    """
    return database.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()


def get_trainer_by_name(database: Session, name: str):
    """
        Find a user by his name
    """
    return database.query(models.Trainer).filter(models.Trainer.name == name).all()


def get_trainers(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all users
        Default limit is 100
    """
    return database.query(models.Trainer).offset(skip).limit(limit).all()


def create_trainer(database: Session, trainer: schemas.TrainerCreate):
    """
        Create a new trainer
    """
    db_trainer = models.Trainer(name=trainer.name, birthdate=trainer.birthdate)
    database.add(db_trainer)
    database.commit()
    database.refresh(db_trainer)
    return db_trainer


def add_trainer_pokemon(database: Session, pokemon: schemas.PokemonCreate, trainer_id: int):
    """
        Create a pokemon and link it to a trainer
    """
    db_item = models.Pokemon(
        **pokemon.dict(), name=get_pokemon_name(pokemon.api_id), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def add_trainer_item(database: Session, item: schemas.ItemCreate, trainer_id: int):
    """
        Create an item and link it to a trainer
    """
    db_item = models.Item(**item.dict(), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def get_items(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all items
        Default limit is 100
    """
    return database.query(models.Item).offset(skip).limit(limit).all()


def get_pokemon(database: Session, pokemon_id: int):
    """
        Find a pokemon by his id
    """
    return database.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()


def get_pokemon_stats(api_id: int):
    """
       Get pokemon stats from pokeapi
    """
    pokemon = get_pokemon_stats_api(api_id)
    return pokemon

def get_pokemons(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all pokemons
        Default limit is 100
    """
    return database.query(models.Pokemon).offset(skip).limit(limit).all()

def fight_pokemon(trainer: models.Trainer, trainer2: models.Trainer):
    """
        Make a fight between 2 trainers
    """
    score_trainer1 = 0
    score_trainer2 = 0

    len_loop = min(len(trainer.pokemons), len(trainer2.pokemons))

    for i in range(len_loop):
        result = battle_pokemon(trainer.pokemons[i].api_id, trainer2.pokemons[i].api_id)

        score_trainer1 += 1 if result['id'] == trainer.pokemons[i].api_id else 0
        score_trainer2 += 1 if result['id'] == trainer2.pokemons[i].api_id else 0

    if score_trainer1 > score_trainer2:
        return {"winner": trainer, "is_tie": False}
    if score_trainer2 > score_trainer1:
        return {"winner": trainer2, "is_tie": False}
    return {"winner": None, "is_tie": True}
