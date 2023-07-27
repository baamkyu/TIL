import sys
input = sys.stdin.readline

def binary_search(start, end, note, check_num):
    while start <= end:
        mid = (start + end) // 2
        if note[mid] == check_num:
            return 1
        elif note[mid] < check_num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

        

T = int(input())
for _ in range(T):
    # 수첩에 적을 수
    N = int(input())
    note = sorted(list(map(int, input().split())))

    # 적혀있는지 확인할 수
    M = int(input())
    check = list(map(int, input().split()))

    for c in check:
        print(binary_search(0, N-1, note, c))