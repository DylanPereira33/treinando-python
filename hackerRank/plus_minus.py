#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

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
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)