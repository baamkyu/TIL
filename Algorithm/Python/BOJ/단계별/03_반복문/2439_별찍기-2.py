# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별을 출력하시오.

N = int(input())
# 1. 
# for i in range(1, N+1):
#     space = ' ' * (N-i)
#     star = '*' * i
#     print(''.join([space, star]))

# 2.
for i in range(1, N+1):
    print(' '* (N-i) + '*' * i)