T = int(input())
for tc in range(1, T+1):
    data = list(input())
    stack = []
    ans = 1
    for i in data:
        if i == '{' or i == '(' or i == ')' or i =='}':
            try:
                if i == '(' or i == '{':
                    stack.append(i)
                elif i == ')' or i == '}':
                    if i == ')' and stack[-1] == '(':
                        stack.pop()
                    elif i == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        break
            except:
                ans = 0
                pass
    if stack:
        ans = 0

    print(f'#{tc} {ans}')


























#
#
# T = int(input())
# for tc in range(1, T+1):
#     data = list(input())
#     ans = 1
#     stack = []
#     for i in range(len(data)):
#         try:
#             if data[i] == '(' or data[i] == '{':
#                 stack.append(data[i])
#             elif data[i] == ')' and stack[-1] == '(':
#                 stack.pop()
#             elif data[i] == '}' and stack[-1] == '{':
#                 stack.pop()
#             else:
#                 ans = 0
#                 break
#         except:
#             pass
#     if len(stack) != 0:
#         ans = 0
#
#     print(f'#{tc} {ans}')