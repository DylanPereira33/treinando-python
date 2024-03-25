import json

number = "number.json"

with open(number) as f:
    fav_number = json.load(f)

print(f"Eu sei qual é o seu número favorito! É {fav_number}")