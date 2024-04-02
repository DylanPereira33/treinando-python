rios = {"Amazonas": "Brasil", "Nilo":"Egito", "Eufrates":"Iraque"}

for rio,país in rios.items():
    print(f"O rio {rio} corre pelo {país}")

print("\n")
for rio in rios.keys():
    print(rio)

print("\n")
for país in rios.values():
    print(país)