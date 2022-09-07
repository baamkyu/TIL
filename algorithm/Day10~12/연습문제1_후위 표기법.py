# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     push_list = ['+', '-', '*', '/']
#     stack = []
#     for i in N:
#         if i in push_list:
#             stack.append(i)
#         else:
#             print(i, end='')
#     for i in range(len(stack)):
#         print(stack.pop(), end='')
#     print()

T = int(input())
cal_lst = ['+', '-', '*', '/']
stack = []
for tc in range(1, T+1):
    arr = input()
    print(f'#{tc }', end = ' ')
    for i in arr:
        if i in cal_lst:
            stack.append(i)
        else:
            print(i, end = '')
    for i in range(len(stack)):
        print(stack.pop(), end = '')
    print()


























