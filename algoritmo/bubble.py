import random

def bubble_sort(list):
  length = len(list)
  for i in range(length-1):
    for j in range(length-1-i):
      if list[j] > list[j+1]:
        list[j],list[j+1] = list[j+1],list[j]

numbers = []
for i in range(100):
    numbers.append(random.randint(0, 100))
bubble_sort(numbers)
nums = [10, 9, 8, 7, 11, 12, 13]
bubble_sort(nums)
print(numbers)
print(nums)