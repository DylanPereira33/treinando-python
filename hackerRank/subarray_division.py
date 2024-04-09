import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    nums_ways = 0
    for i in range(len(s)-m+1):
        segment = s[i:i+m]
        if sum(segment) == d:
            nums_ways += 1
     
    return nums_ways
        
    
    

