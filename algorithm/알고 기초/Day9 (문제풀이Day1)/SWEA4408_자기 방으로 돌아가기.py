import sys
sys.stdin = open('SWEA4408_자기 방으로 돌아가기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    now_lst = []
    goal_lst = []
    for _ in range(N):
        now, goal = map(int, input().split())
        now_lst.append(now)
        goal_lst.append(goal)
    cnt = 1
    for i in range(N//2+1):
        print(i)
    for i in range(N//2+1):
        for j in range(N//2+1):
            if j != i and now_lst[i] >= now_lst[j] and now_lst[i] <= goal_lst[j] and goal_lst[i] >= now_lst[i] and goal_lst[i] >= goal_lst[j]:
                cnt += 1
            if j != i and now_lst[i] >= now_lst[j] and now_lst[i] <= goal_lst[j] and goal_lst[i] >= now_lst[i] and goal_lst[i] <= goal_lst[j]:
                cnt += 1
            if j != i and now_lst[i] <= now_lst[j] and now_lst[i] <= goal_lst[j] and goal_lst[i] >= now_lst[j] and goal_lst[i] >= goal_lst[j]:
                cnt += 1
            if j != i and now_lst[i] <= now_lst[j] and now_lst[i] <= goal_lst[j] and goal_lst[i] >= now_lst[j] and goal_lst[i] <= goal_lst[j]:
                cnt += 1
    print(f'#{tc} {cnt}')