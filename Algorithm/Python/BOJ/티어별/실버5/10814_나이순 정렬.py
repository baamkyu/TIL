N = int(input())
inf = []
for _ in range(N):
  age, name = input().split()
  inf.append([int(age), name])
inf.sort(key= lambda inf: inf[0])

for i in inf:
  print(i[0], i[1])