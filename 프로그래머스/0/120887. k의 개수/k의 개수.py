def solution(i, j, k):
    answer = 0
    for z in range(i,j+1):
        if str(z).count(str(k)) > 0:
            answer += str(z).count(str(k))
    return answer