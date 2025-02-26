def solution(strArr):
    answer = {}

    for word in strArr:
        leng = len(word)
        if leng not in answer:
            answer[leng] = []
        answer[leng].append(word) 

    return max(len(i) for i in answer.values()) 