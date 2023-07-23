import sys
input = sys.stdin.readline

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * N

for n in range(N):
    visited = [False for _ in range(N)]
    for grade in range(5):
        for id in range(N):
            if id != n and classes[id][grade] == classes[n][grade]:
                visited[id] = True
    cnt[n] = len(list(filter(lambda x: x, visited)))
print(cnt.index(max(cnt)) + 1)