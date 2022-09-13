import sys
sys.stdin = open('SWEA4864_문자열비교.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    small_S = input()
    big_S = input()
    if small_S in big_S:  # big_S 안에 small_S가 있으면 1, 없으면 0출력
        print(f'#{tc} {1}')
    else: print(f'#{tc} {0}')