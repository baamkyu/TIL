def change(n):
    num = 0
    cnt = 0
    while num != n:
        ans_lst = []
        for i in range(-1, -20, -1):
            if num + 1 * (2**i) < n:
                num = num + 1 * (2 ** i)
                ans_lst.append(1)
                cnt += 1
            elif num + 1 * (2 ** i) > n:
                ans_lst.append(0)
                cnt += 1
            elif num + 1 * (2 ** i) == n:
                ans_lst.append(1)
                return ans_lst

        if len(ans_lst) >= 13:
            return 'overflow'
        else:
            return ans_lst


T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc}', end=' ')
    for i in change(N):
        print(i, end='')
    print()