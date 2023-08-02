N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
check = list(map(int, input().split()))

for c in check:
    is_find = False
    s, e = 0, N-1
    while s <= e:
        mid = (s+e) // 2
        if c < card[mid]:
            e = mid - 1
        elif c > card[mid]:
            s = mid + 1
        else:
            is_find = True
            break
    if is_find:
        print(1, end = ' ')
    else:
        print(0, end = ' ')