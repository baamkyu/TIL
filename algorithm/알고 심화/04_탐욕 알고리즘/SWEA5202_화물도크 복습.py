T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = []           # s, e를 리스트로 담아줄 빈 리스트 생성
    for _ in range(N):  # s, e를 빈 리스트에 담아줌
        s, e = list(map(int, input().split()))
        time.append([s,e])

    time.sort(key=lambda time: time[1])


    check = time.pop(0)     # 비교할 값을 첫번째 인자로 담아줌
    ans = 1                 # 첫번째 화물이 들어가있으니까 1부터 시작
    while time:
        if check[1] <= time[0][0]:  # 조건을 만족하면 ans += 1, 첫번째 인자로 담아뒀던 기준값을 변경해줌
            ans += 1
            check = time.pop(0)
        else:
            time.pop(0)             # 조건을 만족하지 않으면 다음 인자로 시도해보기 위해 pop
    print(f'#{tc} {ans}')
