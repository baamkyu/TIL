# 1의 개수를 카운트하는 함수
def count_one(n):
    one = bin(n).count('1')
    return one

# 다음 큰 수 구하는 함수
def solution(n):
    answer = n
    while True:
        answer += 1
        if count_one(n) == count_one(answer):
            break
    return answer

print(solution(78))