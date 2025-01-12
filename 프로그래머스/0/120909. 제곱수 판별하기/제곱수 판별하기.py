import math

def solution(n):
    k = str(math.sqrt(n))
    return 1 if int(k[k.index('.') + 1]) == 0 else 2