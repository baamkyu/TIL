T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N//10
    def dp_function(n):
        # n이 1인 경우
        if n == 1:
            return 1
        
        # n이 2인 경우
        if n == 2:
            return 3
        
        # dp 테이블 초기화
        dp = [0] * (n+1)
        dp[1], dp[2], dp[3] = 1, 3, 5
        
        # dp 테이블 채우기
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]*2
        
        return dp[n]

    print(f'#{tc} {dp_function(n)}')
