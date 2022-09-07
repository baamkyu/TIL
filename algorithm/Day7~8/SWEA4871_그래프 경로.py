import sys
sys.stdin = open('SWEA4871_그래프 경로.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # Vertex, Edge 입력
    adj_matrix = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):                  # 2차원 리스트에 표시
        start, end = map(int, input().split())
        adj_matrix[start][end] = 1

    S, G = map(int, input().split())    # 출발 노드, 도착 노드
    stack = [S]                         # stack에 출발노드 입력해놓음
    visited = []
    ans = 0
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

        for destination in range(V+1):
            if adj_matrix[current][destination] == 1 and destination not in visited:
                stack.append(destination)
    if G in visited:
        ans = 1
    print(f'#{tc} {ans}')





