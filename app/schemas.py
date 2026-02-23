"""
Pydantic schemas for the Pokemon Trainer API.

Defines the data models for trainers, pokemons, items, and battles.
"""

from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

class ItemBase(BaseModel):
    """Base schema for items."""
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """Schema for creating items."""
    pass

class Item(ItemBase):
    """Schema for item response."""
    id: int
    trainer_id: int

    class Config:
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):
    """Base schema for pokemons."""
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """Schema for creating pokemons."""
    pass

class Pokemon(PokemonBase):
    """Schema for pokemon response."""
    id: int
    name: str
    trainer_id: int

    class Config:
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel):
    """Base schema for trainers."""
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """Schema for creating trainers."""
    pass

class Trainer(TrainerBase):
    """Schema for trainer response."""
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        orm_mode = True

#
#  BATTLE
#
class BattleResult(BaseModel):
    """Schema for battle results."""
    winner: Optional[Trainer] = None
    is_tie: bool

    class Config:
        orm_mode = True
