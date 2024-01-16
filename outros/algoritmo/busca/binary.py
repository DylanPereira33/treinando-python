# Gerando lista ordernada
import random
numbers = []
for i in range(10_000):
    numbers.append(random.randint(1,1_000))
numbers.sort()

# Algoritmo de busca
alvo = 600 
fim = len(numbers)
inicio = 0

while inicio < fim:
    meio = int((inicio + fim)/2)
    if numbers[meio] > alvo:
        fim = meio - 1
    elif numbers[meio] < alvo:
        inicio = meio + 1
    else:
        print(meio)