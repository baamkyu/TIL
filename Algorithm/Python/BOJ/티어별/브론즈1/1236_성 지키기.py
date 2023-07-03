# 영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다.
# 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.
# 성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())  # N: 성의 가로 크기, M: 성의 세로 크기 (50보다 작거나 같은 자연수)
castle = [list(input()) for _ in range(N)]
col = 0
row = 0
for i in range(N):
    if 'X' not in castle[i]:
        row += 1

for j in range(M):
    if 'X' not in [castle[i][j] for i in range(N)]:
        col += 1
print(max(row, col))