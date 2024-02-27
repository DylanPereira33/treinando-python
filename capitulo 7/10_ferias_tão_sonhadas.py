respostas = {}
dream = True

while dream:
    name = input("Qual é o seu nome?")
    place = input("Se pudesse visitar qualquer lugar do mundo,para onde iria?")

    respostas[name] = place

    repete = input("gostaria de chamar alguem para particiar do teste? (yes / no)")
    if repete == "no":
        dream = False

print("\npesquisa completa!")
for name,place in respostas.items():
    print(f"{name} gostaria deir para {place}")