T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    # 부분집합 찾기
    subsets = [0]
    for height in heights:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + height)
    print(subsets)
    # 최소차 찾기
    ans = []
    for subset in subsets:
        if subset >= B:
            ans.append(subset - B)
    print(f'#{tc} {min(ans)}')

