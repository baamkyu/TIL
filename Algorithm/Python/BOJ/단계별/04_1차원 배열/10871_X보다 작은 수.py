# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

#1. 
# N, X = map(int, input().split())
# arr = list(map(int, input().split()))
# temp = []
# for i in range(N):
#     if arr[i] < X:
#         temp.append(arr[i])
# a = ' '.join(map(str, temp))
# print(a)

#2.
N, X = map(int, input().split())
arr = list(map(int, input().split()))
temp = []
for i in range(N):
    if arr[i] < X:
        print(arr[i], end = ' ')