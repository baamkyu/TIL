arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# 열 우선 순회
n=3
m=4
for j in range(m):
    for i in range(n):
        print(arr[i][j])

# 지그재그 순회
n=3
m=4
for i in range(n):
    for j in range(m):
        arr[i][j] + (m-1-2*j) * (i%2) # 1 2 3 4 8 7 6 5 9 10 11 12
                                      # 행 번호가 짝수면 i%2에서 [i][j]로 된다.
                                      # 행 번호가 홀수인 경우에 [i][j+(m-1-2*j)]