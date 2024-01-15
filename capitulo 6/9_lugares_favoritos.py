favorite_places = {"Dylan":["Japão","Alemanha"],"Derick":["Brasil","França"],"Luke":["Portugal","Inglaterra"] }

for nome,lugares in favorite_places.items():
    print(f"O lugar favorito do {nome} é ")
    for lugar in lugares:
        print("\t" + lugar)
