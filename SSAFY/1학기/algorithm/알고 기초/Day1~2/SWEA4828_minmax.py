import sys
sys.stdin = open('input_4828.txt', 'r')

T = int(input())
for tc in range(1, T+1): # 출력값에서 tc를 1부터 써야하기 때문에 1부터 범위 지정
    N = int(input())
    number = list(map(int, input().split()))
    num_max = 0
    num_min = 1000000 # num의 범위 0~1000000, 최대값은 0으로 시작, 최소값은 1000000으로 시작
    for j in number:
        if j>num_max: # 최대값 구하기
            num_max = j
        if j<num_min: # 최소값 구하기
            num_min = j
    gap = num_max - num_min # 최대값 - 최소값
    print(f'#{tc} {gap}')