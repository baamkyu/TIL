T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N:수강생의 수, K:과제를 낸 사람의 수
    yes_list = map(int, input().split())
    check_list = list(range(1, N+1))
    for i in yes_list:
        if i in check_list:
            check_list.remove(i)
    print(f'#{tc}', end = ' ')
    print(*check_list)