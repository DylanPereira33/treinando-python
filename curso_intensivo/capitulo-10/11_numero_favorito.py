import json

number = "number.json"

fav_number = input("Qual é o seu número favorito?")

with open(number,"w") as f:
    json.dump(fav_number,f)