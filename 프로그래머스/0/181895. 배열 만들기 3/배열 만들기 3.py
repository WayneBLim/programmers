def solution(arr, intervals):
    return [item for i in intervals for item in arr[i[0]:i[1]+1]]