import sys
input = sys.stdin.readline

def binary_search(s, e, note, check):
    while s <= e:
        mid = (s + e) // 2
        if note[mid] == check:
            return 1
        elif note[mid] < check:
            s = mid + 1
        else:
            e = mid - 1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    note = sorted(list(map(int, input().split())))

    M = int(input())
    check = list(map(int, input().split()))

    for c in check:
        print(binary_search(0, N-1, note, c))