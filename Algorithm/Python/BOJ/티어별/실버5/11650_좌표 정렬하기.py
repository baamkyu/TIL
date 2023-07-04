N = int(input())
coors = []
for _ in range(N):
    coor = list(map(int, input().split()))
    coors.append(coor)

coors.sort()

for i in coors:
    for j in i:
        print(j, end = ' ')
    print('')