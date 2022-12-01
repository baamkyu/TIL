arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

bit = [0] * n   # bit[i] = arr[i]가 부분집합의 원소인지 표시
def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end = ' ')
        print()
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)


f(0,n)