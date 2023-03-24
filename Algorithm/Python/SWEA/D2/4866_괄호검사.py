def check():
    stack = []
    for i in arr:
        if i == '(' or i == '{':
            stack.append(i)
        if i == ')' or i == '}':
            if stack:
                x = stack.pop()
            else:
                return 0
            if i == ')' and x == '{':
                return 0
            if i == '}' and x == '(':
                return 0
    if stack:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    arr = input()
    print(f'#{tc} {check()}')
