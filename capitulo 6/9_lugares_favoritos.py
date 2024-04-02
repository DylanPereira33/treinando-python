favorite_places = {"Dylan":["Japão"],"Derick":["Brasil","França"],"Luke":["Portugal","Inglaterra", "Itália", "Holanda", "Hungria"] }

for nome,lugares in favorite_places.items():
    if len(lugares) == 0:
        print(f"{nome} gosta de ficar em casa")
    elif len(lugares) == 1:
        print(f"O lugar preferido do usuário {nome} é {lugares[0]}")
    else:
        *inicio, ultimo = lugares
        print(f"Os lugares favoritos do usuário {nome} são: ", end= "")
        print(*inicio, sep=", ",end=" e ")
        print(ultimo)