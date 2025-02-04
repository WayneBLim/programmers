def solution(hp):
    k = hp//5
    j = (hp%5)//3
    i = ((hp%5)%3)//1
    return k+j+i