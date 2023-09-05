import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    com = sys.stdin.readline().split()
    # 정수 X를 스택에 넣는 연산이다.
    if com[0] == 'push':
        stack.append(com[1])
    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif com[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # 스택에 들어있는 정수의 개수를 출력한다.
    elif com[0] == 'size':
        print(len(stack))
    # 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif com[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif com[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])