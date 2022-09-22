'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''
# 교수님 코드 - 재귀순열
# arr = ['A', 'B', 'C']     # 재료 리스트
# sel = [0, 0, 0]           # 인형뽑기 selection
# check = [0, 0, 0]         # 뽑을지 말지 결정하는 리스트
#
#
# def perm(depth):    # 각자 뎁스에서는? 꿈안의 꿈(인셉션)-- ㅡ # depth : len(check)
#     if depth == 3:  # 최고 뎁스에 도달했으면? # if depth == len(sel)
#         print(sel)  # print
#         return
#
#     for i in range(3):  # 3번의 화살표 떨어트릴 기회
#         if not check[i]:  # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
#             check[i] = 1  # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
#             sel[depth] = arr[i]  # 화살표가 떨어진 위치의 재료리스트
#             perm(depth+1)
#             check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)
#
# perm(0)

# # 영록님
# def perm(depth, current, acc):
#     global answer
#     # if acc >= answer:     # 백트래킹
#     #     return
#     if depth == N-1:
#         answer = min(answer, acc+acc[current][0])
#         return
#     for i in range(N):
#         if not check[i]:
#             check[i] = 1
#             perm(depth+1, i, acc+acc[current][i])
#             check[i] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     answer = 1000
#     check = [0] * N
#     check[0] = 1
#     perm(0, 0, 0)
#     print(f'#{tc} {answer}')


def goback(start, cnt, root_cnt):
    global min_cnt
    # 최대 경로에 도달 했다면, 리턴
    if root_cnt == N-1:
        cnt += matrix[start][0]
        if cnt < min_cnt:
            min_cnt = cnt
        cnt -= matrix[start][0]
        return

    # 진행중인 카운트가 최소 값보다 크다면, 리턴
    if cnt > min_cnt:
        return

    # 현재 위치에 도달
    visited[start] = 1

    root_cnt += 1
    for i in range(N):
        if not visited[i] and i != start:
            cnt += matrix[start][i]
            goback(i, cnt, root_cnt)
            cnt -= matrix[start][i]
    visited[start] = 0
    root_cnt -= 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_cnt = 100*(N+1)
    visited = [0]*N
    goback(0, 0, 0)

    print('#{} {}'.format(tc, min_cnt))







# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     e = [list(map(int, input().split())) for _ in range(N)]
#     ans = []
#
#     if N == 3:
#         for i in range(1, N):    # N = 3인 경우 1 - 2~3순열 - 1
#             for j in range(1, N):
#                 if i != j:
#                     ans.append(e[0][i] + e[i][j] + e[j][0])
#         print(f'#{tc} {min(ans)}')
#
#     if N == 4:
#         for i in range(1, N):    # N = 4인 경우 1 - 2~4순열 - 1
#             for j in range(1, N):
#                 if i != j:
#                     for k in range(1, N):
#                         if i != k and j != k:
#                             ans.append(e[0][i] + e[i][j] + e[j][k] + e[k][0])
#
#         print(f'#{tc} {min(ans)}')