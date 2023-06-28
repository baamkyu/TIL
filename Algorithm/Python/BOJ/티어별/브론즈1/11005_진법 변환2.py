# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35, 최대 36진법까지 가능!

N, B = map(int, input().split())   # N : 주어진 수, B : 진법
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

num = N
ans = ''
while num > 0:
    ans += tmp[num%B]
    num //= B
print(ans[::-1])