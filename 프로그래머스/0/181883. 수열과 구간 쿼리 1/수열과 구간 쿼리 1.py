def solution(arr, queries):
    for i in queries:
        for j in range(i[0],i[1]+1):
            arr[j] += 1
    return arr
