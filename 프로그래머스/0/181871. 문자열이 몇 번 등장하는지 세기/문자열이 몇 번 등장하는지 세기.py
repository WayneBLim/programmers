def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if myString[i:i+len(pat)].count(pat):
            answer += 1
    return answer