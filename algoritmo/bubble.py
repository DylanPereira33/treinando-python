numbers = [2,8,6,10,7,5,9,4,3,1]
n = len(numbers)

for pos_inicial in range(n-1):
    for pos_atual in range(n-1-pos_inicial):
      if numbers[pos_atual] > numbers[pos_atual+1]:
        numbers[pos_atual],numbers[pos_atual+1] = numbers[pos_atual+1],numbers[pos_atual]
print(numbers)