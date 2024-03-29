'''
x^n 을 구하는 것
ex. 2^7 = 2^3 * 2^3 * 2
ex. 2^8 = 2^4 * 2^4 로 나타낼 것임
'''

def recursive_power(x, n):
    if n == 1:
        return x

    # 짝수승인 경우
    if not n % 2:
        y = recursive_power(x, n/2)
        return y*y

    # 홀수승인 경우
    if n % 2:
        y = recursive_power(x, (n-1)/2)
        return y*y*x

print(recursive_power(2, 7))