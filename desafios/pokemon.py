import requests
import json

class Pokemon:
    def __init__(self):
        self.base_experience = 0
x = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
j = json.loads(x.text)


print(Pokemon(**j).__dict__)