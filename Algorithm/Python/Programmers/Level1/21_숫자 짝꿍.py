import sys
input = sys.stdin.readline

X, Y = map(str, input().split())

x_list = list(map(int, X))
y_list = list(map(int, Y))

x = [0] * 10
y = [0] * 10

for i in x_list:
    x[i] += 1
for i in y_list:
    y[i] += 1

temp = []
for i in range(10):
    if x[i] >= 1:
        if y[i] >= 1:
            temp.append(str(i) * min(x[i], y[i]))

if len(temp) == 0:
    print('-1')
else:
    print(''.join(temp)[::-1])

