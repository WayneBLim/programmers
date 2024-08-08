def solution(array):
    max_number = max(array)
    answer = []

    for i in array:
        if i == max_number:
            answer.append(i)
            answer.append(array.index(i))
            
    return answer