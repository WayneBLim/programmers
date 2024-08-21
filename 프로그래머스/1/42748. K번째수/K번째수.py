def solution(array, commands):
    answer = []
    temp = []
    for i in commands:
        temp = array[i[0]-1 : i[1]]
        temp.sort()
        answer.append(temp[i[2]-1])

    return answer