def solution(myString, pat):
    return myString[ :myString.rfind(pat)+len(pat)]