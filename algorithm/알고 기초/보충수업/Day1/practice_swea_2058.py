pw, num = list(map(int, input().split()))
try_num = 1
while pw != num:
    try_num += 1
    num += 1
print(try_num)