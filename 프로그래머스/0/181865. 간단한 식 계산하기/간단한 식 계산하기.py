def solution(binomial):
    temp = binomial.split()
    a = int(temp[0])
    b = int(temp[2])

    if temp[1] == '+':
        return a + b
    elif temp[1] == '-':
        return a - b
    elif temp[1 == '*']:
        return a * b