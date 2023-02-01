def solution(n):
    answer = ''

    while n > 0:			
        n, m = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer += str(m)
    return int(answer, 3)