import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())    # 아이템의 수 m, 큐 연산의 수 n
    arr = list(input().split())
    non_check = arr[:]  # 얕은 복사
    temp = ['x'] * m

    for _ in range(n):
        a, b = map(int, input().split())
        temp[b-1] = arr[a-1]
        non_check.remove(arr[a-1])

    for i in range(m):
        if temp[i] == 'x':
            temp[i] = non_check[0]
            non_check.pop(0)
    print(*temp)