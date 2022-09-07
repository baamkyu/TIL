import sys
sys.stdin = open('SWEA1210_ladder.txt', 'r')
T = 10
for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    visited = []

    for j in range(100):
        if data[99][j] == 2:
            now_i = 99
            now_j = j

    while now_i > 0:
        tmp = [now_i, now_j]
        visited.append(tmp)
        # visited += [[now_i, now_j]]

        if now_j-1 >= 0 and data[now_i][now_j-1] == 1 and [now_i, now_j-1] not in visited:
            now_j -= 1

        elif now_j+1 < 100 and data[now_i][now_j+1] == 1 and [now_i, now_j+1] not in visited:
            now_j += 1

        else:
            now_i -= 1

    print(f'#{tc} {now_j}')



# T = 10
# for tc in range(1, 11):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(100)]
#     for j in range(100):
#         if data[99][j] == 2:
#             now_i = 98
#             now_j = j
#
#     while now_i > 0:
#         if now_j > 0 and data[now_i][now_j-1] == 1:
#             while data[now_i][now_j-1] == 1:
#                 now_j -= 1
#                 if now_j == 0:      # 왼쪽 끝이면 break
#                     break
#             now_i -= 1
#         elif now_j < 99 and data[now_i][now_j+1] == 1:
#             while data[now_i][now_j+1] == 1:
#                 now_j += 1
#                 if now_j == 99:     # 오른쪽 끝이면 break
#                     break
#             now_i -= 1
#         else:
#             now_i -= 1
#
#     print(f'#{tc} {now_j}')


# visited 활용
# T = 10
# for tc in range(1, 11):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(100)]
#     for j in range(100):
#         if data[99][j] == 2:
#             now_i = 98
#             now_j = j
#             visited = []
#     while now_i > 0:
#         if data[now_i][now_j-1] == 1 and now_j < 99 and (now_i, now_j-1) not in visited:
#             visited += (now_i, now_j-1)
#             now_j += 1
#         elif data[now_i][now_j+1] == 1 and now_j > 0 and (now_i, now_j+1) not in visited:
#             visited += (now_i, now_j+1)
#             now_j -= 1
#         else:
#             now_i -= 1
#     print(f'#{tc} {now_j}')