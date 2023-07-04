# 입력값 받기
N = int(input())
xys = []    # (키, 몸무게) 리스트
for _ in range(N):
  x, y = map(int, input().split())
  xys.append((x, y))

ranks = []  # 등수 리스트
for i in xys:
  rank = 1
  for j in xys:
    if i[0] < j[0] and i[1] < j[1]:   # 다른 사람보다 덩치가 작으면 등수 + 1
      rank += 1
  ranks.append(rank)
print(*ranks)