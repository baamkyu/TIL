# 서로 인접한 좌석 사이에는 컵홀더가 하나씩 있고, 양 끝 좌석에는 컵홀더가 하나씩 더 있다. 또, 이 극장에는 커플석이 있다. 커플석 사이에는 컵홀더가 없다.
# S는 일반 좌석, L은 커플석을 의미하며, L은 항상 두개씩 쌍으로 주어진다.
# 어떤 좌석의 배치가 SLLLLSSLL일때, 컵홀더를 *로 표시하면 다음과 같다. ex) *S*LL*LL*S*S*LL*

N = int(input())
seats = list(input())
S_cnt = L_cnt = 0
for seat in seats:
    if seat == 'L':
        L_cnt += 1
    if seat == 'S':
        S_cnt += 1

cup = 1 + S_cnt + L_cnt//2

if cup < N:
    print(cup)
else:
    print(N)