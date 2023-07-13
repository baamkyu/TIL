# 피제수(분자) A와 제수(분모) B가 있다. 두 수를 나누었을 때, 소숫점 아래 N번째 자리수를 구하려고 한다.
A, B, N = map(int, input().split())
num = A % B  # 나머지 계산
for _ in range(N - 1):  # N번째 자리까지 나머지를 10을 곱해주고 다시 나누기
    num = (num * 10) % B
print((num * 10) // B)  # 몫 출력