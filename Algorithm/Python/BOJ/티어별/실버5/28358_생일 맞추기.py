# 많은 사람이 아이디를 지을 때 생일과 관련된 숫자를 넣지만, 찬우의 아이디에서 등장하는 숫자는 태어난 달이나 태어난 일에 등장하는 숫자들과 하나도 겹치지 않는다.
# 찬우의 아이디에 어떤 숫자가 포함되어 있는지 주어지면, 찬우의 생일이 될 수 있는 날짜의 수를 구해보자.
# 찬우가 태어난 해는 윤년이다. 즉, 찬우의 생일은 2월 29일이 될 수도 있다. 또한 태어난 달이나 일이 한 자리라면 십의 자리는 빈 칸으로 생각한다.

import sys
input = sys.stdin.readline

T = int(input())

day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for _ in range(T):
    arr = list(map(int, input().split()))
    possible_num = []
    for i in range(10):
        if arr[i] == 0:
            possible_num.append(i)

    ans = 0
    days31 = [1, 3, 5, 7, 8, 10, 12]
    days30 = [4, 6, 9, 11]
    days29 = [2]
    for i in possible_num:
        for j in possible_num:
            if i in days31:
                if j <= 31 and j != 0:
                    ans += 1
                if int(str(i) + str(j)) <= 31 and int(str(i) + str(j)) >= 10:
                    ans += 1
            elif i in days30:
                if j <= 30 and j != 0:
                    ans += 1
                if int(str(i) + str(j)) <= 30 and int(str(i) + str(j)) >= 10:
                    ans += 1
            elif i == 2:
                if j <= 29 and j != 0:
                    ans += 1
                if int(str(i) + str(j)) <= 29 and int(str(i) + str(j)) >= 10:
                    ans += 1
    print(ans)