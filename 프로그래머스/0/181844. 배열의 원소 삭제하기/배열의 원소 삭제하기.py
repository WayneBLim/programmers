def solution(arr, delete_list):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in delete_list:
            answer.append(arr[i])
            print(answer)
    return answer