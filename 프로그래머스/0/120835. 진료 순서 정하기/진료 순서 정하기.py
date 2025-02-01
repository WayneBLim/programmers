def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(temp.index(i)+1)
    return answer