def solution(myString):

    k = sorted(myString.split('x'))
    return [i for i in k if i != '']