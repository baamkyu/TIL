import sys
sys.stdin = open('sum_input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    column_sum = []
    row_sum = []
    rightdown_sum = 0
    leftdown_sum = 0
    all_sum = []
    for c in range(100): # 열 (세로)
        row_hap = 0
        column_hap = 0
        rightdown_sum += arr[c][c] # 오른쪽 대각선
        leftdown_sum += arr[c][99-c] # 왼쪽 대각선
        for r in range(100): # 행 (가로)
            row_hap += arr[c][r]
            column_hap += arr[r][c]
        row_sum += [row_hap] # 각 행의 합 리스트
        column_sum += [column_hap] # 각 열의 합 리스트
    all_sum = row_sum + column_sum + [rightdown_sum] + [leftdown_sum]   # 각 행, 각 열, 오른쪽 대각선, 왼쪽 대각선 합의 리스트

    max_A = 0
    for i in all_sum: # all_sum 중 최대값 구하기
        if max_A < i:
            max_A = i
    print(f'#{tc} {max_A}')
    # print(row_sum)
    # print(column_sum)
