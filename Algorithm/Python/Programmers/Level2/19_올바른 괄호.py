def solution(s):
    answer = True
    stackCount = 0
    for i in s:
        if i == '(':
            stackCount += 1
        elif i == ')':
            stackCount -= 1
        if stackCount < 0:
            return False
    if stackCount == 0:
        return True
    else:
        return False
    