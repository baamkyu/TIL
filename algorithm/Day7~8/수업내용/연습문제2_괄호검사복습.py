T = int(input())
for tc in range(1, T+1):
    data = list(input())
    stack = []
    ans = 1
    for i in range(len(data)):
        if data[i] == '(':
            stack.append('(')
        else:
            try:
                stack.pop()
            except:
                ans = -1
        print(data)
        print(stack)
    if len(stack) != 0:
        ans = -1
    print(f'#{tc} {ans}')