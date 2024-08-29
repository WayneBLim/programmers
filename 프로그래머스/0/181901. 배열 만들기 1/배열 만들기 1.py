def solution(n, k):
    answer = []
    i = 1
    while 1:
        j = k * i 
        if j <= n:
            answer.append(j)
            i += 1
        else:
            return answer