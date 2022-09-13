import sys
sys.stdin = open('input.txt')

testcase = 10
for tc in range(1, testcase+1):
    N = int(input())
    row = list(map(int, input().split()))

    cnt_row = 0
    for i in range(2, N-2): # 양 옆으로 2칸씩은 지어지지 않으므로 범위지정
        max_row = 0

        if row[i]>row[i-1] and row[i]>row[i-2] and row[i]>row[i+1] and row[i]>row[i+2]: # 조망권 확보 조건
            for j in (row[i-1], row[i-2], row[i+1], row[i+2]):
                if max_row < j:
                    max_row = j
            cnt_row += row[i] - max_row
    print(f'#{tc} {cnt_row}')