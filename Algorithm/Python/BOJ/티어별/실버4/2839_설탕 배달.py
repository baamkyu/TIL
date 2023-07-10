# 설탕 봉지는 3kg, 5kg 두 종류가 있다.
# 상근이가 설탕을 정확하게 Nkg 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하라.
N = int(input())
ans = -1
# 3kg 봉지는 최소로, 5kg 봉지는 최대로 해야 최소 봉지 수가 나옴
# 따라서 3kg 봉지는 작은 수부터 시작, 5kg 봉지는 큰 수부터 시작
for i in range(N//3+1):             # 0 ~ N//3 까지 오름차순
    rem = N - 3*i
    for j in range(rem//5, -1, -1): # 3kg봉지를 뺀 나머지에서 5로 나눈걸 0까지 내림차순
        if 5 * j + 3 * i == N:
            ans = i + j
            break
    if ans > 0:
        break
print(ans)