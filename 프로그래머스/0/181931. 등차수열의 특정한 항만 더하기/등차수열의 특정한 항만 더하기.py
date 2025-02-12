def solution(a, b, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a + b * i
    return answer