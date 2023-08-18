# import sys
# input = sys.stdin.readline

# # sol 1. 내가 푼 풀이 (시간초과)

# lst = list(input())
# for i in range(len(lst)):
#     if lst[i] == '(' and lst[i+1] == ')':
#         lst[i] = 'x'
#         lst[i+1] = 'x'

# head = []   # 파이프 앞의 위치
# tail = []   # 파이프 끝의 위치
# razer = []  # 레이저 위치
# pipe = []   # head와 tail의 짝

# for i in range(len(lst)):
#     if lst[i] == '(':
#         head.append(i)
#     elif lst[i] == ')':
#         tail.append(i)
#     elif lst[i] == 'x':
#         razer.append(i)
# print(head, tail)
# # 파이프의 짝 찾아주기
# for t in tail:
#     for h in head[::-1]:
#         if t > h:
#             head.remove(h)
#             pipe.append([h, t])
#             break
        
# # 정답 구하기
# # 잘랐을 때의 파이프의 수 = 기본 파이프의 수 + 잘린 횟수
# ans = len(pipe)   # 기본 파이프의 수를 넣고 시작

# # 파이프를 레이저로 잘랐을 때 나누어지면 + 1
# for r in razer[::2]:
#     for p in pipe:
#         if p[0] < r and p[1] > r:
#             ans += 1
# print(ans)

# sol 2. 인터넷 찾아본 풀이
import sys
input = sys.stdin.readline

lst = list(input())
stack = []
ans = 0

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append('(')
    else:
        if lst[i-1] == '(':   # () 이 연속으로 나오는 경우
            stack.pop()
            ans = ans + len(stack)
        else:                 # ')' 이 나오는 경우
            stack.pop()
            ans += 1  # 파이프 생성되었기 때문
print(ans)