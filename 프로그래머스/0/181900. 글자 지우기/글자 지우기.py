def solution(my_string, indices):
    indices.sort()
    my_string=list(my_string)

    for i in indices[-1::-1]:
        del my_string[i]
    return ''.join(my_string)