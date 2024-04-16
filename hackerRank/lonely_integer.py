def lonelyInteger(a):
    for num in a:
        if a.count(num) == 1:
            return num

def lonelyIntegerFast(a):
    result = {}
    for num in a:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    for num in result.keys():
        if result[num] == 1:
            return num