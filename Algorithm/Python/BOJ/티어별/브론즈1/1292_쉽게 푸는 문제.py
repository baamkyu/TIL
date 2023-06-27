A, B = map(int, input().split())

check = 0     # 배열 내의 숫자 개수 (숫자가 몇까지 필요한지 확인하기 위해)
lastnum = 0   # 배열에 필요한 마지막 숫자
# 어디까지 숫자가 필요한지 찾기
for i in range(1, 1000):
    check += i
    lastnum += 1
    if B <= check:
        # print(lastnum)
        break
# 필요한 수까지의 배열 만들기
arr = []
for i in range(1, lastnum+1):
    for j in range(i):
        arr.append(i)
# 배열 중 원하는 부분의 합 구하기
ans = sum(arr[A-1:B])
print(ans)