def perm(depth):
    temp2 = temp[:]
    if depth == N-1:
        lst.append(temp2)
        return

    for i in range(N-1):
        if not visited[i]:
            visited[i] = 1
            temp[depth] = i + 1
            perm(depth+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    # input값
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 재귀 위해서 변수 선언
    temp = [0] * (N-1)
    visited = [0] * (N-1)
    lst = []
    perm(0)

    for i in range(len(lst)):       # 앞뒤로 0을 넣어줌
        lst[i] = [0] + lst[i] + [0]
    ans = 1000      # 최소값 담을 변수
    for i in range(len(lst)):       # N = 3 이면 0120 0210
        temp = 0
        for j in range(N):
            temp += arr[lst[i][j]][lst[i][j + 1]]   # 모르겠으면 print(lst) 찍어보기
        ans = min(ans, temp)
    print(f'#{tc} {ans}')


#     lst[0] = 0 1 2 0
#     lst[1] = 0 2 1 0
# 01 12 23
# N은 근데 0 1 2