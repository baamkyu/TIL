# 세준이는 기말고사를 망쳐서 점수를 조작하려고 한다.
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다.
# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

N = int(input())  # 시험 과목 수
scores = list(map(int, input().split()))  # 과목별 시험 점수
max_score = max(scores)
for i in range(N):
    scores[i] = scores[i] / max_score * 100
print(sum(scores) / len(scores))