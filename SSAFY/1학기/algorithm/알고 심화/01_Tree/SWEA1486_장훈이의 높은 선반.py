T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    members_height = list(map(int, input().split()))
    S = sum(members_height)

    # 부분집합 모음
    subsets = [0]
    for member_height in members_height:
        size = len(subsets)
        for i in range(size):
            subsets.append(subsets[i]+member_height)

    # 최소차 찾기
    ans = []
    for i in range(len(subsets)):
        if subsets[i] >= B:
            ans.append(subsets[i] - B)

    print(f'#{tc} {min(ans)}')