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
   
    def test_battle_compare_stats(self):
        first_pokemon_stats = [
            {'base_stat': 45, 'stat': {'name': 'hp'}},
            {'base_stat': 49, 'stat': {'name': 'attack'}},
            {'base_stat': 49, 'stat': {'name': 'defense'}}
        ]
        second_pokemon_stats = [
            {'base_stat': 39, 'stat': {'name': 'hp'}},
            {'base_stat': 52, 'stat': {'name': 'attack'}},
            {'base_stat': 43, 'stat': {'name': 'defense'}}
        ]
    
        result = battle_compare_stats(first_pokemon_stats, second_pokemon_stats)
        assert result == 1
        
        def test_battle_pokemon_first_wins(self, mocker):
            """Test quand le premier pokemon gagne"""
            mocker.patch('app.utils.pokeapi.get_pokemon_data', side_effect=[
                {'name': 'pikachu', 'stats': [{'base_stat': 50}]},
                {'name': 'bulbasaur', 'stats': [{'base_stat': 40}]}
            ])
            
            result = battle_pokemon("25", "1")
            assert result['name'] == 'pikachu'

        def test_battle_pokemon_second_wins(self, mocker):
            """Test quand le second pokemon gagne"""
            mocker.patch('app.utils.pokeapi.get_pokemon_data', side_effect=[
                {'name': 'pikachu', 'stats': [{'base_stat': 40}]},
                {'name': 'bulbasaur', 'stats': [{'base_stat': 50}]}
            ])
            mocker.patch('app.utils.pokeapi.battle_compare_stats', return_value=-1)
            
            result = battle_pokemon("25", "1")
            assert result['name'] == 'bulbasaur'

        def test_battle_pokemon_draw(self, mocker):
            """Test en cas de match nul"""
            mocker.patch('app.utils.pokeapi.get_pokemon_data', side_effect=[
                {'name': 'pikachu', 'stats': [{'base_stat': 45}]},
                {'name': 'bulbasaur', 'stats': [{'base_stat': 45}]}
            ])
            mocker.patch('app.utils.pokeapi.battle_compare_stats', return_value=0)
            
            result = battle_pokemon("25", "1")
            assert result == {'winner': 'draw'}