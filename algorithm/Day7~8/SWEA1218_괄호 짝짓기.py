import sys
sys.stdin = open('SWEA1218_괄호 짝짓기.txt', 'r')

T = 10
for tc in range(1, T+1):
    len_data = int(input())
    data = list(input())
    stack = []
    ans = 1
    for i in range(len(data)):
        if data[i] == '(' or data[i] == '{' or data[i] == '[' or data[i] == '<':
            stack.append(data[i])
        elif data[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif data[i] == '>' and stack[-1] == '<':
            stack.pop()
        elif data[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif data[i] == '}' and stack[-1] == '{':
            stack.pop()
        else:
            ans = 0

    if stack:   # stack 안에 원소가 들어있으면 ans = 0
        ans = 0

    print(f'#{tc} {ans}')
