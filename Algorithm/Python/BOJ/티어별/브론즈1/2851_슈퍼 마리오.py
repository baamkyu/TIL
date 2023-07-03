# # 10개의 수가 주어지는데 처음부터 연속된 수를 더해서 100에 가장 가까운 수를 만들어라.

# # 입력값 받아서 리스트로 만들기
# mush = []
# for _ in range(10):
#     m = int(input())
#     mush.append(m)

# # 100에 가까운 수를 찾음
# tmp = []
# score = 0
# for i in mush:
#     score += i
#     if score >= 100:
#         if score - 100 > 100 - (score - i):
#             score -= i
#         break
# print(score)

arr = []
for i in range(10):
    arr.append(int(input()))

sum_arr = 0

for i in range(len(arr)):
    sum_arr += arr[i]
    if sum_arr == 100:
        print(sum_arr)
        break
    elif sum_arr > 100:
        if 100 - sum(arr[:i]) >= sum_arr - 100:
            print(sum_arr)
            break

        else:
            print(sum(arr[:i]))
            break
