def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            answer = answer[:-arr[i]]
    return answer