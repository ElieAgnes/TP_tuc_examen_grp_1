import pytest
from app.utils.pokeapi import get_pokemon_name, battle_compare_stats, battle_pokemon

class TestPokeApi():
    
    def test_get_pokemon_name(self, mocker):
        mocker.patch(
            'app.utils.pokeapi.get_pokemon_data',
            return_value={"name": "bulbasaur"}
        )
        result = get_pokemon_name("1")
        assert result == "bulbasaur"
    
    
    