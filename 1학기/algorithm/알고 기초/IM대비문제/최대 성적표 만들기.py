T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    score_lst = list(map(int, input().split()))
    sort_score_lst = sorted(score_lst)
    tmp_lst = []

    for i in range(1, K+1):
        tmp_lst.append(sort_score_lst[-i])
    print(f'#{tc}', end = ' ')
    print(sum(tmp_lst))