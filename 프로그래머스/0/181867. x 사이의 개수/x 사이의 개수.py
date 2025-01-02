def solution(myString):
    myString = myString.split("x")
    return [len(i) for i in myString]