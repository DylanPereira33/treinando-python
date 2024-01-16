# numbers = [2,8,6,10,7,5,9,4,3,1]


    # n = len(lista)
    # for pos_inicial in range(n-1):
    #     menor_pos = pos_inicial
    #     for i in range(n):
    #         if lista[i] < lista[menor_pos]:
    #             menor_pos = i
    #     if lista[pos_inicial] > lista[menor_pos]:
    #         pos_inicial = menor_pos

 
# for pos_inicial in range(len(numbers)):
#         menor_pos = pos_inicial
#         for index in range(pos_inicial+1, len(numbers)):
#             if numbers[menor_pos] > numbers[index]:
#                 menor_pos = index
#         numbers[menor_pos], numbers[pos_inicial] = numbers[pos_inicial], numbers[menor_pos] 
# print(numbers)        


numbers = [2,8,6,10,7,5,9,4,3,1]

n = len(numbers)
for pos_inicial in range(n):
    min_pos = pos_inicial
    for index in range(pos_inicial+1, n):
       if numbers[min_pos] >  numbers[index]:
        min_pos = index
    numbers[min_pos], numbers[pos_inicial] = numbers[pos_inicial], numbers[min_pos]
print(numbers)


