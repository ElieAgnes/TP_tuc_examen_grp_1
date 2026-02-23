"""
Schemas module defining the Pydantic models for trainers, pokemons, and items
"""

from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel):# pylint: disable=too-few-public-methods
    """
    Base class for an item
    """
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):# pylint: disable=too-few-public-methods
    """ 
    Class for creating an item
    """

class Item(ItemBase):# pylint: disable=too-few-public-methods
    """
    Class representing an item in the database
    """
    id: int
    trainer_id: int

    class Config:# pylint: disable=too-few-public-methods
        """
        Configuration for Pydantic model to work with SQLAlchemy models
        """
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):# pylint: disable=too-few-public-methods
    """
    Base class for a pokemon
    """
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):# pylint: disable=too-few-public-methods
    """
    Class for creating a pokemon
    """

class Pokemon(PokemonBase):# pylint: disable=too-few-public-methods
    """
    Class representing a pokemon in the database
    """
    id: int
    name: str
    trainer_id: int

    class Config:# pylint: disable=too-few-public-methods
        """
        Configuration for Pydantic model to work with SQLAlchemy models
        """
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel):# pylint: disable=too-few-public-methods
    """
    Base class for a trainer
    """
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):# pylint: disable=too-few-public-methods
    """
    Class for creating a trainer
    """

class Trainer(TrainerBase):# pylint: disable=too-few-public-methods
    """
    Class representing a trainer in the database
    """
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:# pylint: disable=too-few-public-methods
        """
        Configuration for Pydantic model to work with SQLAlchemy models
        """
        orm_mode = True

#
#  BATTLE
#
class BattleResult(BaseModel):# pylint: disable=too-few-public-methods
    """
    Class representing the result of a battle between 2 trainers
    """
    winner: Optional[Trainer] = None
    is_tie: bool

    class Config:# pylint: disable=too-few-public-methods
        """
        Configuration for Pydantic model to work with SQLAlchemy models
        """
        orm_mode = True
