from datetime import datetime

def solution(date1, date2):
    c = datetime(date1[0], date1[1], date1[2]).strftime('%Y-%m-%d')
    d = datetime(date2[0], date2[1], date2[2]).strftime('%Y-%m-%d')

    if c < d:
        return 1
    else:
        return 0