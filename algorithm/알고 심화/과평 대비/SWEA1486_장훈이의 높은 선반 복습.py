T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    subsets = [0]
    for height in heights:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + height)

    ans = []
    for i in range(len(subsets)):
        if subsets[i] >= B:
            ans.append(subsets[i])
    print(f'#{tc} {min(ans) - B}')