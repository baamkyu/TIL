T = int(input())
for tc in range(1, T+1):
    input = input()
    stack = []
    is_perfect = 0  # 올바른 괄호인지 확인
    for i in input:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                is_perfect = 0
    if stack:
        pass 
    else:
        is_perfect = 1
print(f'#{tc} {is_perfect}')