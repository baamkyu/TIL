def solution(n):
    count = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                count += 1
                break
            elif sum > n:
                break 
    return count

# 완전 탐색, 효율을 높이기 위해 sum > n일 때 동작을 그만하게 설계