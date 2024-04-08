favorite_places = {"Dylan":["Japão","Alemanha"],"Derick":["Brasil",],"Luke":["Portugal","Inglaterra","França","Alemanha"] }

for nome,lugares in favorite_places.items():
    if len(lugares) == 0:
        print(f"{nome} não gosta de lugares")
    if len(lugares) == 1:
        print(f"O lugar favorito do {nome} é {lugares[0]}")
    if len(lugares) > 1:
        *inicio, ultimo = lugares
        print(f"Os lugares favoritos do {nome} são: ", end="")
        print(*inicio, sep=", ", end= " e ")
        print(ultimo)
    
    
