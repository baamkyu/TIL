# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다.
import sys
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{tc}: {a+b}')