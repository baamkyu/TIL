# # stack 구현
# def push(item, size):
#     global top
#     top += 1
#     if top == size:  # stack에서의 위치가 top이면
#         print('overflow!')
#     else:
#         stack[top] = item
#
# size = 10
# stack = [0] * size  # size크기만큼 배열 생성
# top = -1
#
# push(10, size)
# top += 1        #push(20)
# stack[top] = 20
#
#
# # 스택의 pop
# def pop():
#     if len(S) == 0:
#         #underflow
#         return
#     else:
#         return s.pop(-1):
#
#
#
#

# 연습문제1 스택 구현
stackSize = 10
stack = [0] * stackSize
top = -1
print(top)      # -1
print(stack)    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

top += 1        # top = 0
stack[top] = 1  # stack[0] = 1
print(top)      # 0
print(stack)    # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

top += 1        # top = 1
stack[top] = 2  # stack[1] = 2
print(top)      # 1
print(stack)    # [1,2,0,0,0,0,0,0,0,0]

top -= 1        # top = 0
temp = stack[top + 1]  # temp = stack[1]
print(top)      # 0
print(stack)    # [1,2,0,0,0,0,0,0,0,0]
print(temp)     # 2

temp = stack[top]
top -= 1
print(top)      # -1
print(stack)    # [1,2,0,0,0,0,0,0,0,0]

stack2 = []
stack2.append(10)
stack2.append(20)
print(stack2)       # [10, 20]
print(stack2.pop())  # 20
print(stack2.pop())  # 10
