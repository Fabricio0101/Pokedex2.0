import requests
import json

class Pokemon():
    def __init__(self, sprite, nomePokemon, type_primary, type_secondary, weight, height, hp, attack, defense, special_attack, special_defense, speed):
        self.nomePokemon = nomePokemon
        self.sprite = sprite
        self.type_primary = type_primary
        self.type_secondary = type_secondary
        self.weight = weight
        self.height = height
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed


def configpokemonName(pokeName):
        pokemonName = pokeName.lower()
        request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
        todo = json.loads(request.content)

        nomePokemon = todo['name'].capitalize()
        spriteTodo = todo['sprites']
        sprite = spriteTodo['other']['official-artwork']['front_default']
        type_primary = todo['types'][0]['type']['name'].capitalize()
        try:
            type_secondary = todo['types'][1]['type']['name'].capitalize()
        except:
            type_secondary = "Nenhum"
        weight = todo['weight']/10
        height = todo['height']/10
        hp = todo['stats'][0]['base_stat']
        attack = todo['stats'][1]['base_stat']
        defense = todo['stats'][2]['base_stat']
        special_attack = todo['stats'][3]['base_stat']
        special_defense = todo['stats'][4]['base_stat']
        speed = todo['stats'][5]['base_stat']

        pokemon = Pokemon(sprite, nomePokemon, type_primary, type_secondary, weight, height, hp, attack, defense, special_attack, special_defense, speed)
        return pokemon

