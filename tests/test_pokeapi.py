import pytest
from fastapi.testclient import TestClient
from app.utils.pokeapi import get_pokemon_name

class TestPokeApi():
    
    def test_get_pokemon_name(self, mocker):
        mocker.patch(
            'app.utils.pokeapi.get_pokemon_name',
            return_value="bulbasaur"
        )
        result = get_pokemon_name("1")
        assert result == "bulbasaur"
    
    
    