'''
1
5 16
1 3 3 5 6
'''



T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # N : 점원수, B : 탑의 높이
    members_height = list(map(int, input().split()))
    S = sum(members_height)

    # 부분집합 모음
    subsets = [0]
    for member_height in members_height:
        size = len(subsets)
        for i in range(size):
            subsets.append(subsets[i] + member_height)
    print(subsets)