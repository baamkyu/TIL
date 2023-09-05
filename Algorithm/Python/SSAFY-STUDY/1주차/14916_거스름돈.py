import sys
input = sys.stdin.readline

n = int(input())
ans = 0

if n % 5 == 0:    # 5원으로만 거슬러줘도 나눠 떨어지는 경우
    ans += n//5
else:             # 2원도 섞어서 줘야하는 경우
    for i in range(n//5, -1, -1):  # 5원을 최대한 많이 줘야해서 큰 수부터 시작
        change = n - i*5          # 2원짜리로만 거슬러줘야하는 액수
        if change % 2 == 0:       # 2원짜리로 가능하다면 ans = 5원짜리 개수 + 2원짜리 개수
            ans += i
            ans += change // 2
            break
        
if ans == 0:
    print(-1)
else:
    print(ans)