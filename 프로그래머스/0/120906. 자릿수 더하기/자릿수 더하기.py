def solution(n):
    list1 = list(str(n))
    answer = 0
    for i in list1:
        answer += int(i)
    return answer