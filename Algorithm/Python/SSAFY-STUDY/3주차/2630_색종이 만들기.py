import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def solution(x, y, N) :
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j]:
        solution(x, y, N//2)        # 왼쪽 위 (제2사분면)
        solution(x, y+N//2, N//2)   # 왼쪽 아래 (제3사분면)
        solution(x+N//2, y, N//2)   # 오른쪽 위 (제1사분면)
        solution(x+N//2, y+N//2, N//2)  # 오른쪽 아래 (제4사분면)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))