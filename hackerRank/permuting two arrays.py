def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    n = len(A)
    for i in range(n):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"