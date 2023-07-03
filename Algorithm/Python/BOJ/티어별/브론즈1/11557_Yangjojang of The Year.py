# 학교별로 한 해동안 술 소비량이 주어질 때, 가장 술 소비가 많은 학교 이름을 출력하여라.
T = int(input())
for _ in range(T):
    N = int(input())
    max_uni = ''   # 술 소비가 가장 많은 학교
    max_soju = 0   # 술 소비의 최대값
    for i in range(N):
        uni, soju = list(input().split())
        if max_soju < int(soju):
            max_soju = int(soju)
            max_uni = uni
    print(max_uni)