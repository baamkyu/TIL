T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = list(map(int, input().split()))

    # 처음에 가장 큰 나무 설정
    max_tree = max(tree)

    # 모든 나무와 가장 큰 나무의 키 차이 확인
    need_height = []
    for i in range(N):
        need_height.append(max_tree - tree[i])
    need_height = sorted(need_height)

    # 필요한 날짜 구하기
    day = 1
    # ans = 0
    last_tree = need_height[-1]  # 마지막 거는 0을 해줘야할수도 있기 때문에 따로 지정해줌

    for need in need_height[:-1]:  # 마지막 제외하고 순회
        while need != 0:
            if need == 1 and day % 2 == 0:  # 1이 필요한데 짝수번째 날이면 제일 큰 수에 -2
                last_tree -= 2
                day += 1
                # ans += 1
            elif need == 2 and day % 2 == 1:    # 2가 필요한데 홀수번째 날이면 제일 큰 수에 -1
                last_tree -= 1
                day += 1
                # ans += 1
            else:
                if day % 2 == 1:     # 홀수번째 날이면
                    need -= 1        # 키 차이가 1 줄어듬
                    day += 1
                    # ans += 1
                elif day % 2 == 0:   # 짝수번째 날이면
                    need -= 2        # 키 차이가 2 줄어듬
                    day += 1
                    # ans += 1

    while last_tree != 0:
        if last_tree == 1 and day % 2 == 0:    # 1이 필요한데 짝수번째 날이면 pass
            day += 1
            # ans += 1
        elif last_tree == 2 and day % 2 == 1:  # 2가 필요한데 홀수번째 날이면 pass
            day += 1
            # ans += 1
        else:
            if day % 2 == 1:    # 홀수번째 날이면
                last_tree -= 1  # 키 차이가 1 줄어듬
                day += 1
                # ans += 1
            elif day % 2 == 0:  # 짝수번째 날이면
                last_tree -= 2  # 키 차이가 2 줄어듬
                day += 1
                # ans += 1

    print(f'#{tc} {day-1}')