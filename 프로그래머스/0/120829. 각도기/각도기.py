def solution(angle):
    if 0 < angle <= 180:
        if 0 < angle < 90:
            return 1
        elif angle == 90:
            return 2
        elif 90 < angle < 180:
            return 3
        elif angle == 180:
            return 4
    else:
        print("다시 입력 하세요")

