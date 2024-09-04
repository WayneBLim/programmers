def solution(s):
    s = [i for i in s]
    answer = reversed(sorted(s))
    return ''.join(answer)