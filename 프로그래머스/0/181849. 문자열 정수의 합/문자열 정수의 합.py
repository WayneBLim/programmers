def solution(num_str):
    final = 0

    for i in range(len(num_str)):
        final += int(num_str[i])
    return final