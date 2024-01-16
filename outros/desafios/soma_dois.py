def twoSum(nums, target):
    length = len(nums)
    for i in range(length-1):
        number = nums[i]
        value = target - number
        for j in range(i+1, length):
            if (value == nums[j]):
                return [i, j]

def fastTwoSum(nums, target):
    dic = {}
    for index, number in enumerate(nums):
        if number in dic.keys():
            return [dic[number], index]
        dic[target - number] = index

print(twoSum([8, 2, 15, 9, 6, -6], 9))
print(fastTwoSum([8, 2, 15, 9, 6, -6], 9))