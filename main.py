"""
Main module for the Pokemon Trainer API.

This FastAPI application provides endpoints for managing trainers, pokemons, items, and battles.
"""

from fastapi import FastAPI
from app.routers import fight, trainers, pokemons, items


app = FastAPI()


app.include_router(trainers.router,
                   prefix="/trainers")
app.include_router(items.router,
                   prefix="/items")
app.include_router(pokemons.router,
                   prefix="/pokemons")
app.include_router(fight.router,
                   prefix="/fight")
