números = {'Luke':[42,13],'Dylan':[33,42],'Derick':[10,15],'Ana':[15,51],'Francisco':[50,20]}

for nome,numeros in números.items():
    print(f"O numero favorito do {nome} é ")
    for numero in numeros:
        print(f"\t  {numero}")
