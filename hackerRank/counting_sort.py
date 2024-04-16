# Time Complexity: O(n)
def countingSort(arr):
    frequency = [0] * 100
    for num in arr:
        frequency[num] += 1
        
    return frequency