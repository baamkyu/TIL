'''
3
2 7
3 15
36 1007
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    cnt = 0
    queue = [N]
    visited = set()

    while M not in queue:
        for _ in range(len(queue)):
            now = queue.pop(0)
            if now not in visited and 0 < now <= 1000000:
                visited.add(now)
                for i in [now+1, now-1, now*2, now-10]:
                    queue.append(i)
                    if i == M:
                        break
        cnt += 1
    print(f'#{tc} {cnt}')