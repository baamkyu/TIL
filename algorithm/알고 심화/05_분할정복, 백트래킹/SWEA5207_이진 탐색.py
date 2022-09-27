def ejin(lst, num, check, ex_check):
    global l, r, cnt
    while True:
        m = (l+r)//2

        # 값을 찾거나 방향이 연속될 때까지 반복
        if ex_check == check:   # 연속된 방향이 같으면 return
            return

        if lst[m] == num:       # 값을 찾으면 cnt+=1 후 return
            cnt += 1
            return

        # 나아갈 방향 확인
        if lst[m] > num:    # 찾을 값이 왼쪽에 있으면 check = 1
            check = ex_check
            ex_check = 1
            r = m - 1

        elif lst[m] < num:  # 찾을 값이 오른쪽에 있으면 check = 2
            check = ex_check
            ex_check = 2
            l = m + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnt = 0

    for i in B:
        if i in A:
            l = 0
            r = len(A) - 1
            ejin(A, i, 0, -1)

    print(f'#{tc} {cnt}')