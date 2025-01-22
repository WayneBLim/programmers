def solution(array, n):
    answer = array[0]
    for i in array:
        if abs(i-n) < abs(n-answer):
            answer = i
        elif abs(i-n) == abs(n-answer):
            answer = min(i,answer)
    return answer