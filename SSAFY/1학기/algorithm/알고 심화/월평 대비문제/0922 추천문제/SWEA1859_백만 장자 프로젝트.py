'''
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    max_arr = max(arr)
    for i in range(0, N-1):
        x = arr[i]
        if x == max_arr:
            max_arr = max(arr[i+1::])
        if x <= max_arr:
            ans += max_arr - x
    print(f'#{tc} {ans}')












    # temp = []
    # ans = 0
    # temp_arr = [0] * N
    # max_arr = max(arr)
    # top = 0
    # for i in range(N):
    #     if arr[i] != max_arr:   # 최대값 나올 때까지 temp에 값을 추가
    #         temp.append(arr[i])
    #
    #     if arr[i] == max_arr:   # 최대값 나오면 temp에 있는 값을 ans에 다 더해줌
    #         for tmp in temp:
    #             ans += tmp
    #
    #         arr.pop(i)          # 최대값 삭제
    #         max_arr = max(arr)  # max_arr값 새로 초기화
    #
    # print(f'#{tc} {ans}')