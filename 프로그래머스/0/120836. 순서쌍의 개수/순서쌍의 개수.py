def solution(n):
    return sum(1 for i in range(1, n+1) if n % i == 0)