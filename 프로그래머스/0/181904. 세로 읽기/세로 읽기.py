def solution(my_string, m, c):
    temp = []
    for i in range(0,len(my_string),m):
        temp.append(my_string[i:i+m][c-1])
    answer = "".join(temp)
    return answer