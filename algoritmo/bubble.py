numbers = [2,8,6,10,7,5,9,4,3,1]
n = len(numbers)

contador = 0
# Complexidade Temporal O(n^2)
for pos_inicial in range(n-1):
    for pos_atual in range(n-1-pos_inicial):
      contador += 1
      if numbers[pos_atual] > numbers[pos_atual+1]:
        numbers[pos_atual],numbers[pos_atual+1] = numbers[pos_atual+1],numbers[pos_atual]

print(numbers)