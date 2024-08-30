def invert_sign(num):
    return -num

def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True:
            continue
        else:
            absolutes[i]=invert_sign(absolutes[i])

    return sum(absolutes)