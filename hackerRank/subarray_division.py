def birthday(s, d, m):
    # Write your code here
    nums_ways = 0
    for i in range(len(s)-m+1):
        segment = s[i:i+m]
        if sum(segment) == d:
            nums_ways += 1
     
    return nums_ways
        
    
    

