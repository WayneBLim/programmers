import math

def solution(n):

    for i in range(1,11):
        if math.factorial(i) < n:
            continue
        elif math.factorial(i) == n:
            return i
        else:
            return i-1