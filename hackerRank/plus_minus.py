def plusMinus(arr):
    # Write your code here
    positive,negative,nulos = (0,0,0)
    n = len(arr)

    for index in range(n):
        if arr[index] > 0:
            positive += 1
        elif arr[index] < 0:
            negative += 1
        else:
            nulos += 1
        
    print(positive/n)
    print(negative/n)
    print(nulos/n)