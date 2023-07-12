# 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.


N = int(input())
N_arr = sorted(list(map(int, input().split()))) # 이 카드에

M = int(input())
M_arr = list(map(int, input().split())) # 이 숫자들이 있는지 없는지 확인 해야함

for m in M_arr:
    start, end = 0, N-1  # 인덱스 범위
    exist = False
    while start <= end:
        mid = (start + end) // 2
        if m > N_arr[mid]: 
            start = mid + 1
        elif m < N_arr[mid]:
            end = mid - 1
        else:
            exist = True
            break

    if exist == False:
        print(0, end= ' ')
    else:
        print(1, end= ' ')


# 시간초과 코드
# N = int(input())
# N_arr = list(map(int, input().split()))
# M = int(input())
# M_arr = list(map(int, input().split()))

# check = [0] * M
# num = 0
# for i in M_arr:
#     if i in N_arr:
#         check[num] = 1
#         num += 1
#     else:
#         check[num] = 0
#         num += 1
# print(*check)