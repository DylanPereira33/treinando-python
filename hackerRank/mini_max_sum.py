#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min,max,sum = arr[0], arr[0], 0
    for i in arr:
        if i < min:
            min = i
        elif i > max:
            max = i
        sum += i
    print(f'{sum-max} {sum-min}')
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)