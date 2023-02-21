T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N//10                           # 가독성을 위해 10으로 나누어줌 (모든 입력값이 10의 배수이기 때문에 가능)
    memo = [1] * n                      # 빈 리스트 생성
    for i in range(0, n):
        if i % 2 != 0:                  # 홀수일 때
            memo[i] = memo[i-1]*2 + 1
        elif i % 2 == 0:                # 짝수일 때
            memo[i] = memo[i-1]*2 - 1
    ans = memo[n-1]
    print(f'#{tc} {ans}')