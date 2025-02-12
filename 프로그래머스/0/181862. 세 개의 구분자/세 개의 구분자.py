import re

def solution(myStr):
    answer = re.split(r'[abc]', myStr)
    answer = [i for i in answer if i != ""]
    if len(answer) == 0:
        answer = ["EMPTY"]

    return answer