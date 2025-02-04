def solution(sides):
    return 1 if sorted(sides)[2]< sorted(sides)[0] + sorted(sides)[1] else 2