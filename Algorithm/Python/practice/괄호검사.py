T = int(input())
for tc in range(1, T+1):
    input = input()
    stack = []              # 여는 괄호('(')를 담을 스택
    is_perfect = 0          # 이상이 없다면 1 출력, 이상있다면 0 출력
    for i in input:
        if i == '(':
            stack.append(i)
            print('stack', stack)
        else:
            stack.pop()
            print(stack)
    if len(stack):
        pass
    else:
        is_perfect = 1
        
    print(f'#{tc} {is_perfect}')
