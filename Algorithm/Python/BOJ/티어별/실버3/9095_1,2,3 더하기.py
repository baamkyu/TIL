T = int(input()) #테스트 케이스 개수

N = [] #n을 저장할 list

for i in range(T):
    N.append(int(input()))

dp = [0,1,2,4] #1,2,3에 대한 값 : 초깃값

for i in range(4, max(N)+1): #4부터 N에 저장된 최댓값까지
    dp.append(dp[i-1]+dp[i-2]+dp[i-3]) 

for n in N:
    print(dp[n])