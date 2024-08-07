def solution(n):
    test = sorted(str(n),reverse=True)

    answer = int(''.join(test))
    return answer