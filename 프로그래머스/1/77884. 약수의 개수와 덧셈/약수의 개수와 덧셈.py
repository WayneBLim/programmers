def solution(left, right):
    answer = 0
    dummy = []
    
    for i in range(left, right+1):
        dummy = []
        for j in range(1,i+1):
            if i % j == 0:
                dummy.append(j)
        if len(dummy) % 2 == 0:
            answer += i
        else:
            answer -= i
        
    return answer
