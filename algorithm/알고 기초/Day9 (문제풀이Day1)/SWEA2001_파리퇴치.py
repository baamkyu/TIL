# import sys
# sys.stdin = open('SWEA2001_파리퇴치.txt', 'r')
#
# T = int(input())
#
# di = [0, 1, 0, -1]  # 시계방향
# dj = [1, 0, -1, 0]
#
# for tc in range(T):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     i = 0
#     j = 0
#     dr = 0
#
import sys
sys.stdin = open('SWEA2001_파리퇴치.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hap_lst = []
    for i in range(N-M+1):                  # 파리채가 구간 안에 다 들어오기 위해 N-M+1을 범위로 설정
        for j in range(N-M+1):
            hap = 0
            for x in range(M):              # i가 나아갈 범위
                for y in range(M):          # j가 나아갈 범위
                    hap += arr[i+x][j+y]    # 모든 수의 합
                    hap_lst.append(hap)    # max함수를 쓰기 위해 리스트로 담아줌
    print(f'#{tc} {max(hap_lst)}')



















