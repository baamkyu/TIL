def partition(A, l, r):  # A : 리스트, l : 왼쪽, r : 오른쪽
    p = A[l]
    i = l+1
    j = r
    while i <= j:
        while (i<=j and A[i]<=p):
            i += 1
        while (i<=j and A[j]>=p):
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def qsort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    qsort(arr, 0, len(arr)-1)
    print(arr)