def solution(a, b):
    j = int(str(a)+str(b))
    k = 2*a*b
    

    print(k,j)
    
    if k <= j:
        return j
    else :
        return k