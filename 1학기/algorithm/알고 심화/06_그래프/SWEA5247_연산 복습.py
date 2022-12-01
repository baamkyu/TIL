# 제한시간 초과
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N를 연산해서 M으로 만들자

    cnt = 0
    visited = set()
    queue = [N]

    while M not in queue:            # queue안에 M이 있을 때까지
        for _ in range(len(queue)):  # queue안에 있는 모든 수를 연산
            now = queue.pop(0)
            if now not in visited and 0 < now <= 1000000:
                visited.add(now)
                for i in [now+1, now-1, now*2, now-10]:
                    queue.append(i)
                    if M in queue:
                        break
        cnt += 1
    print(f'#{tc} {cnt}')

# 통과
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N를 연산해서 M으로 만들자

    ans = 0             # 연산 횟수 담을 변수
    queue = [M]         #
    visited = set()     # 연산해서 나왔던 숫자 기억

    while N not in queue:   # queue에 N이 나올 때까지 돌린다
        for _ in range(len(queue)):
            now = queue.pop(0)  # 현재 위치
            if now not in visited and 0 < now <= 1000000:
                visited.add(now)
                if now % 2 == 0:
                    queue.append(now // 2)
                queue.append(now + 10)
                queue.append(now - 1)
                queue.append(now + 1)

                if N in queue:
                    break
        ans += 1
    print(f'#{tc} {ans}')