def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

for i in range(1, 21):
    print(f'{i}! == {fac(i)}')