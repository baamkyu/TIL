# 2차원 배열 입력, 출력
N=int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
print(arr)

# N*N 배열 2차원 배열 선언하기
for i in range(N):
    for j in range(N):
        print(arr[i][j])
    print()

# N*M 배열 2차원 배열 선언하기
for i in range(N):
    for j in range(M):
        print(arr[i][j])
    print()

# len으로 선언 가능
for i in range(len(arr)): # 행의 개수
    for j in range(len(arr[0])): # 한 행이 주어짐 (=열의 개수)
        print(arr[i][j])
    print()