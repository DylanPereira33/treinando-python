def miniMaxSum(arr):
    min,max,sum = arr[0], arr[0], 0
    for i in arr:
        if i < min:
            min = i
        elif i > max:
            max = i
        sum += i
    print(f'{sum-max} {sum-min}')