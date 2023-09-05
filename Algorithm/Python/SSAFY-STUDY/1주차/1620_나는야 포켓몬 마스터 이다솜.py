import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poketmon = {}
for i in range(1, N+1):
    name = input().split()[0]
    poketmon[i] = name  # ex. {1: 'pica'}
    poketmon[name] = i  # ex. {'pica': 1}

for _ in range(M):
    find = input().split()[0]
    if find.isdigit():  # 정수인 경우
        print(poketmon[int(find)])
    else:
        print(poketmon[find])