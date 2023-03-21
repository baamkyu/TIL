T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 배열의 길이
    arr = list(map(int, input().split()))
    answer = 0 # 최대낙차 기록용
    for i in range(n):
        cnt = 0 # 현재 아이템의 낙차
        for j in range(i, n):
          if (arr[i] > arr[j]):
            cnt += 1
        if answer < cnt:
           answer = cnt
    print(f'#{tc} {answer}')
