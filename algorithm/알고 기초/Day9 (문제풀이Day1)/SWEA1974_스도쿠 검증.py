import sys
sys.stdin = open('SWEA1974_스도쿠 검증.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    cnt_x = []
    cnt_y = []
    cnt = 0
    ans = 0
    standard = [i for i in range(1,10)]

    for i in range(9):
        cnt_x = []
        cnt_y = []
        for j in range(9):
            cnt_x.append(arr[i][j])     # 가로 검증
            cnt_y.append(arr[j][i])     # 세로 검증
        if sorted(cnt_x) == standard:
            cnt += 1
        if sorted(cnt_y) == standard:
            cnt += 1

    # 3x3 검증
    for i in [0,3,6]:
        for j in [0,3,6]:
            temp_lst = []
            for k in range(3):
                for l in range(3):
                    temp_lst.append(arr[k][l])
            if sorted(temp_lst) == standard:
                cnt += 1

    if cnt == 27:
        ans = 1

    print(f'#{tc} {ans}')


