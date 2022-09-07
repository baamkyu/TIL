T = int(input())
for tc in range(1, T+1):
    y = int(input())        # 삼각형의 높이
    arr = []
    big_arr = []
    for i in range(y):      # 모든 원소가 0인 삼각형 생성
        arr = [0] * (i+1)
        for j in range(len(arr)):   # 앞과 뒤를 1로 설정
            arr[0] = 1
            arr[-1] = 1
        big_arr.append(arr)         # 2차원 리스트 big_arr을 생성


    for i in range(len(big_arr)):           # 2차원 리스트의 모든 범위
        for j in range(len(big_arr[i])):
            if big_arr[i][j] == 0:          # 0인 값만 재설정 => 앞과 뒤를 1로 설정 했고 안쪽부분만 더하면 되기 때문
                try:
                    big_arr[i][j] = big_arr[i-1][j-1] + big_arr[i-1][j]
                except:
                    pass

    print(f'#{tc}')
    for i in range(len(big_arr)):
        print(*big_arr[i])


## 동인님 코드
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     pascal = [[1], [1, 1]]
#     if N > 2:
#         index_N = N-1
#         tmp = [1] * (N-2)
#         for i in range(1, index_N):
#             try:
#                 for j in range(1, index_N):
#                     tmp += [pascal[i][j-1] + pascal[i][j]]
#                 tmp += [1]
#                 pascal += [tmp]
#             except:
#                 pass
#         print(pascal)