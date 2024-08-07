def solution(my_string, n):
    test = list(my_string)
    len_range = len(test)
    test2 = []

    for i in range(len_range):
        test2.append(test[i]*n)
        answer = ''.join(test2)

    return answer