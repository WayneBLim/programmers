def solution(before, after):
    if ''.join(sorted(before)) == ''.join(sorted(after)):
        return 1
    else:
        return 0