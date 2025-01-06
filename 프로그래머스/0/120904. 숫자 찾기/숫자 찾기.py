def solution(num, k):
    return str(num).find(f'{k}')+1 if str(num).find(f'{k}') >= 0 else -1