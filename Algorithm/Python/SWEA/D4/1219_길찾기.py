for _ in range(10):
    tc, N = map(int, input().split())           # testcase번호, N의 개수 input

    load = list(map(int, input().split()))      # input list

    stack = [0]                                 # 출발점 : 0
    visited = [0]                               # 0부터 시작하니까 0방문 저장

    ans = 0

    while stack:
        start = stack.pop()

        if start not in visited:                # 방문하지 않았다면 방문
            visited.append(start)
        
        if start == 99:                         # 99라면 ans = 1으로 끝
            ans = 1
            break

        for i in range(0, len(load), 2):        # 출발, 도착 한 쌍이 2개씩이므로 2개씩 건너 뜀
            if load[i] == start:                # 출발점을 찾으면
                if load[i+1] not in visited:    # 다음 도착지를 이미 방문했었는지 확인
                    stack.append(load[i+1])     # 방문하지 않았다면 추가
    
    print(f'#{tc} {ans}')