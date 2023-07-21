# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.


import sys
input = sys.stdin.readline

# 방법1. 이분탐색 이용
N = int(input())
N_arr = sorted(list(map(int, input().split())))

M = int(input())
M_arr = list(map(int, input().split()))

for i in M_arr:
    left, right = 0, N-1
    isFind = False  # 찾았는지 여부

    while left <= right:
        mid = (left + right) // 2
        if i == N_arr[mid]:
            isFind = True
            print('1')
            break
        elif i > N_arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
            
    if not isFind:
        print(0)

# 방법2
N = int(input())
N_arr = set(list(map(int, input().split())))

M = int(input())
M_arr = list(map(int, input().split()))

for i in M_arr:
    if i in N_arr:
        print(1)
    else:
        print(0)