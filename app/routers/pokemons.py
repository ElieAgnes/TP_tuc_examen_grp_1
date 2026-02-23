from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
import random

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons


@router.get("/random")
def get_random_pokemons(database: Session = Depends(get_db)):
    """
        Return 3 pokemons randomly
    """

    pkm1_api_id = random.randint(1, 898)
    pkm2_api_id = random.randint(1, 898)
    pkm3_api_id = random.randint(1, 898)

    pokemon1 = actions.get_pokemon_stats(pkm1_api_id)
    pokemon2 = actions.get_pokemon_stats(pkm2_api_id)
    pokemon3 = actions.get_pokemon_stats(pkm3_api_id)

    return [pokemon1, pokemon2, pokemon3]