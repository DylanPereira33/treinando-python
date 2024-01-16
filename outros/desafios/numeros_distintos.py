def tem_distintos(nums):
    found = set() 
    for number in nums:
        if number in found:
            return True
        found.add(number)    
    return False

print(tem_distintos([1, 1, 3, 4])) # true
print(tem_distintos([1, 2, 3, 4])) # false
print(tem_distintos([15, 4, 3, 15, 9, 7, 101, 134])) # true
print(tem_distintos([15, 4, 3, 1, 9, 7, 101, 134, 99, 42, 25, 64])) # false
print(tem_distintos([1, 1, 3, 1, 9, 7, 101, 134, 1001])) # true