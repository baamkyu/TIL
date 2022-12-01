'''
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 신청서 N개

    use_time = []       # 리스트로 입력 값 받기
    for i in range(N):
        s, e = map(int, input().split())    # 시작시간 s, 종료시간 e
        use_time.append([s, e])

    use_time.sort(key=lambda x : x[1])      # e 기준으로 정렬

    check = use_time.pop(0)     # 비교할 첫번째 값을 담아줌
    cnt = 1     # 하나 담겨있기 때문에 1부터 시작

    while use_time:
        if use_time[0][0] >= check[1]:
            check = use_time.pop(0)
            cnt += 1
        else:
            use_time.pop(0)
    print(f'#{tc} {cnt}')