'''
상하좌우로 이동할 수 있음
이동하려는 방이 현재 방보다 1 커야함
근데 테스트케이스 이해가 안 된다
'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
