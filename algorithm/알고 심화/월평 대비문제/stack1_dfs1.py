adjList = [[1,2],   # 0
           [0,3,4], # 1
           [0,4],   # 2
           [1,5],   # 3
           [1,2,5], # 4
           [3,4,6], # 5
           [5]]     # 6

def dfs(v):     # v: 시작 지점
    global top
    visited[v] = 1      # 시작 지점 방문 표시
    while True:         # stack에 값이 들어있으면 (맞나??)
        for w in adjList[v]:    # if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0: # 방문 안 한 정점 w가 있으면
                top += 1        # push(v)
                stack[top] = v  #
                v = w           # w에 방문
                print(v)        # 방문한 걸 프린트
                visited[w] = 1  # w에 방문한걸 표시
                break
        else:           # w가 없으면
            if top != -1:   # stack이 비어있지 않은 경우
                v = stack[top]
                top -= 1
            else:           # stack이 비어있으면
                break       # while을 빠져 나옴

N = int(input())
visited = [0] * N   # 방문한 곳 표현
stack = [0] * N     # stack => stack이 비어있으면 프린트
top = -1            # 현재 위치

dfs(0)