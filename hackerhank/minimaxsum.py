#!/bin/python3

import math
import os
import random
import re
import sys

# Complexidade Temporal O(n)
def miniMaxSum(arr):
    min, max, sum = arr[0], arr[0], 0
    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num
        sum += num
    print(f'{sum-max} {sum-min}')


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
