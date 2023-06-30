# 10개의 수가 주어지는데 처음부터 연속된 수를 더해서 100에 가장 가까운 수를 만들어라.

# 입력값 받아서 리스트로 만들기
mush = []
for _ in range(10):
    m = int(input())
    mush.append(m)

# 100에 가까운 수를 찾음
tmp = []
score = 0
for i in mush:
    score += i
    if score >= 100:
        if score - 100 > 100 - (score - i):
            score -= i
        break
print(score)