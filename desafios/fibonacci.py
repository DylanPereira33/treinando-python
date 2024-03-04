fibs = { 1: 0, 2: 1 }
def fibonacci_fast(n):
    global fibs
    if n in fibs:
        return fibs[n]
    result = fibonacci_fast(n-1) + fibonacci_fast(n-2)
    fibs[n] = result
    return result

def fibonacci_slow(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

def fibonacci_non_recursive(n):
    a, b = 0, 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b
