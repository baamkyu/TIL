import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))

place = []
for i in range(1, N+1):
    if i in line:
        if i == line[0]:
            line.remove(i)
        else:
          while i != line[0]:
              place.append(line[0])
              line.pop(0)
              if i == line[0]:
                  line.remove(i)
                  break
    else:
        if i == place[-1]:
            place.pop()

if len(place) == 0 and len(line) == 0:
    print('Nice')
else:
    print('Sad')