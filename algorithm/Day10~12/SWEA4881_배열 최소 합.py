def sum_up(check, stock, n):                                # 재귀용 함수
    global sum_list                                         # sum_list에 합을 넣어줄 거임
    if n >= N:                                              # 반환할 조건은 n이 N에 도달했을 때
        sum_list += [sum(stock)]                            # 지금까지 뽑아놓은 숫자의 합을 더한다.
    elif len(sum_list) <= 1 or sum(stock) < min(sum_list):  # 첫번째 시도이거나, 현재까지의 합이 첫 시도 아래인 경우
        for i in range(N):
            if check[i] == 0:
                stock += [board[n][i]]
                check[i] = 1
                sum_up(check, stock, n+1)
                check[i] = 0
                del stock[len(stock)-1]     # 넣었떤 숫자


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_lst = []    # 가능한 모든 부분집합을 모아둘 공간
    visited = []    # 겹치지 않게 하기 위해
    for i in range(N):
        for j in range(N):
            for k in range(N):
                visited.append(i)
                visited.append(j)
                visited.append(k)
    print(visited)
                # if i != j and j != k and k != i:
                #     print([arr[n][i], arr[n][j], arr[n][k]])