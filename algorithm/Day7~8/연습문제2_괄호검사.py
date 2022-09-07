# T = int(input())
# for tc in range(1, T+1):
#     input_lst = input()
#     level = 0
#     rst = 1
#     for i in input_lst:
#         if i == '(':
#             level += 1
#         if i == ')':
#             level -= 1
#         if level < 0:
#             rst = -1
#     if level != 0:
#         rst = -1
#     print(f'#{tc} {rst}')

import sys
sys.stdin = open('연습문제2_괄호검사.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    lst_input = list(input())
    stack = []
    test = 1
    for i in lst_input:
        if i == '(':
            stack.append('(')
        else:
            try:
                stack.pop()
            except:
                test = -1

    if len(stack) != 0:
        test = -1
    print(f'#{tc} {test}')
















