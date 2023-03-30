# 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
T = 10
for tc in range(1, T+1):
    num = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    row_sum_list = []     # 행의 합 모음
    col_sum_list = []     # 열의 합 모음
    diag_sum = 0          # 대각선의 합
    reverse_diag_sum = 0  # 역대각선의 합
    for i in range(N):
        diag_sum += arr[i][i]
        row_sum = 0
        col_sum = 0
        for j in range(N):
            if (i+j == N):  # 역대각선에 있으면 더해줌
                reverse_diag_sum += arr[i][j]
            row_sum += arr[i][j]  # 한 행의 합
            col_sum += arr[j][i]  # 한 열의 합
        row_sum_list.append(row_sum)  # 한 행의 값을 모두 더한 값을 리스트에 추가
        col_sum_list.append(col_sum)  # 한 열의 값을 모두 더한 값을 리스트에 추가
    print(f'#{num} {max(max(row_sum_list), max(col_sum_list), reverse_diag_sum, diag_sum)}')

        


