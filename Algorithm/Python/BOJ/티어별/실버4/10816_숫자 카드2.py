# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# sol1. 딕셔너리 사용
from collections import Counter

N = int(input())
nums = list(map(int, input().split()))  # 가지고 있는 숫자 카드
M = int(input())
ms = list(map(int, input().split()))    # 개수를 알고 싶은 숫자

# 가지고 있는 숫자카드를 딕셔너리로 생성
dict = {}
for num in nums:
    if num in dict: # 이미 딕셔너리에 생성된 key값이면 value + 1
        dict[num] += 1
    else:           # 딕셔너리에 생성되지 않은 key값이면 key값 생성 후 1로 초기화
        dict[num] = 1
# 개수를 알고 싶은 숫자 출력
for m in ms:
    if m in dict:   # 보유한 숫자카드이면 value값 출력
        print(dict[m], end = ' ')
    else:           # 보유하지 않은 숫자카드이면 0 출력
        print(0, end = ' ')




# sol2. Counter 사용
# from collections import Counter

# N = int(input())
# nums = sorted(list(map(int, input().split())))  # 가지고 있는 숫자 카드
# M = int(input())
# ms = list(map(int, input().split()))    # 개수를 알고 싶은 숫자

# cnt = Counter(nums)

# for i in ms:
#     print(cnt[i], end = ' ')