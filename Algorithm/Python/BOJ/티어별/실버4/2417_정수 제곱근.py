def binary_search(s, e, n):
    while s <= e:
        mid = (s+e) // 2
        if mid ** 2 == n:
            return mid
        elif mid ** 2 < n:
            s = mid + 1
        else:
            e = mid - 1
    return s

import sys
input = sys.stdin.readline

N = int(input())
print(binary_search(0, 2**63, N))