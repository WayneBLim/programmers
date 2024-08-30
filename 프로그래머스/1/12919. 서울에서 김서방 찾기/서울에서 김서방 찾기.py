def solution(seoul):
    for i in seoul:
        if "Kim" in seoul:
            return f"김서방은 {seoul.index('Kim')}에 있다"