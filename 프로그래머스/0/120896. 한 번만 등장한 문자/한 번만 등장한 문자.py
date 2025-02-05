def solution(s):
    k = set(s)
    answer = ''
    for i in k:
        if s.count(i) == 1:
            answer += i
    return ''.join(sorted(answer))