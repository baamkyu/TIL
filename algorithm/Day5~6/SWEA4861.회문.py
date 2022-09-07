import sys
sys.stdin = open('SWEA4861_회문.txt', 'r')

T = int(input())
for tc in range(1, T+1):  # N*N 행렬 만들기
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    turn_matrix = list(zip(*matrix))  # 90도로 회전한 행렬
    answer = ''
    for i in range(N):
        for j in range(N-M+1):
            if matrix[i][j:j+M] == matrix[i][j:j+M][::-1]:
                answer = matrix[i][j:j+M]
            if turn_matrix[i][j:j+M] == turn_matrix[i][j:j+M][::-1]:
                answer = turn_matrix[i][j:j+M]
            # if matrix[i][j:j + M] == list(reversed(matrix[i][j:j + M])):
            #     str1 = matrix[i][j:j + M]
            #
            # if turn_matrix[i][j:j + M] == list(reversed(turn_matrix[i][j:j + M])):
            #     str2 = turn_matrix[i][j:j + M]
    answer = ''.join(answer)
    print(f'#{tc} {answer}')





# import sys
# sys.stdin = open('SWEA4861_회문.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     matrix = [list(map(str, input())) for _ in range(N)]
#     turn_matrix = list(zip(*matrix))
#     str1 = ''
#     str2 = ''
#     for i in range(N):
#         for j in range(N-M+1):
#             if len(matrix[i][j]) == M:
#                 if matrix[i][j] == list(reversed(matrix[i][j:j+M+1])):
#                     str1 = ''.join(matrix[i][j:j+M+1])
#
#     for i in range(N):
#         for j in range(N-M+1):
#             if len(turn_matrix[i][j:j+M+1]) == M:
#                 if turn_matrix[i][j:j+M+1] == list(reversed(turn_matrix[i][j:j+M+1])):
#                     str2 = ''.join(turn_matrix[i][j:j+M+1])
#     print(str1)
#     print(str2)
