def solution(x):
    answer = 0
    for i in str(x):
        answer += int(i)
    if x % answer == 0:
        return True
    else:
        return False