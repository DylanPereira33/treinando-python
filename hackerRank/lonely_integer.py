def lonelyinteger(a):
    # Write your code here
    for num in a:
        if a.count(num) == 1:
            return num

