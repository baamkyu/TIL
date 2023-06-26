# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

C = int(input())
for _ in range(C):
    score = list(map(int, input().split()))
    n = score.pop(0)  # 첫번째로 인풋 받은 것은 점수가 아닌 학생수이므로 score에서 빼가지고 n에 담아준다.
    avg = sum(score) / n
    good_student = 0  # 평균을 넘는 학생 수
    for i in score:
        if i > avg:
            good_student += 1
    percent = round(good_student / n * 100, 3)
    print(f'{percent:.3f}%')