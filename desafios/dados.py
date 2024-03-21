# 3d6+2
# sum = 10
# '[5, 1, 2] + 2 = 10'

# 4d2+1
# sum = 10
# '[1, 1, 2, 1] + 1 = 6'

from random import randint

resultados = []

while True:
    comando = input("Digite qualquer dado (ou 'quit' para encerrar): ")

    if comando.lower() == 'quit':
        break

    result = comando.split("d")
    qtd_dados = int(result[0])
    result1 = result[1].split("+")  
    qtd_faces = int(result1[0]) 

    sum = 0
    mult = 0
    if len(result1) > 1:  
        sum = int(result1[1]) 
        
    elif (len(result1) == 1):
        result1 = result[1].split("-")
        mult=-1


    total = 0
    for _ in range(qtd_dados):
        total += randint(1, qtd_faces)

    resultado_final = total + mult
    resultados.append(resultado_final)

    print("Resultado da rolagem:", resultado_final)

print("Resultados armazenados:", resultados)

    


















