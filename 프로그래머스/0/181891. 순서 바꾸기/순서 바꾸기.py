def solution(num_list, n):
    answer = []
    for i in range(n, len(num_list)):
        answer.append(num_list[i])
    for j in range(n):
        answer.append(num_list[j])
    return answer