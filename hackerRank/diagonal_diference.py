# Time Complexity: (n)
def diagonalDifference(arr):
    # Write your code here
    right_sum = 0
    left_sum = 0
    for i in range(len(arr)):
        right_sum += arr[i][i]
        left_sum += arr[i][len(arr) - i - 1]
    
    absolute_difference = abs(right_sum - left_sum)
    return absolute_difference
    