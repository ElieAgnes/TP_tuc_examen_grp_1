"""
    This module contains functions to interact with the pokeapi API
"""

import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats_api(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    pokemon = get_pokemon_data(api_id)
    return {pokemon['name']: pokemon['stats']}

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premier_pokemon = get_pokemon_data(first_api_id)
    second_pokemon = get_pokemon_data(second_api_id)
    battle_result = battle_compare_stats(
        premier_pokemon['stats'], second_pokemon['stats']
    )

    if battle_result > 0:
        winner = premier_pokemon
    elif battle_result < 0:
        winner = second_pokemon
    else:
        winner = {'winner': 'draw'}
    return winner


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    battle_result = 0
    for i, first_stat in enumerate(first_pokemon_stats):
        second_stat = second_pokemon_stats[i]
        if first_stat['base_stat'] > second_stat['base_stat']:
            battle_result += 1
        elif first_stat['base_stat'] < second_stat['base_stat']:
            battle_result -= 1
    return battle_result
