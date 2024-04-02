import json

number = "number.json"
try:
    with open(number) as f:
        fav_number = json.load(f)
except FileNotFoundError:
    fav_number = input("Whats is your favorite number?")
    with open(number,"w") as f:
        json.dump(fav_number, f)
        print(f"{fav_number} save")
else:
    print(f"{fav_number}, is your favorite number!")
