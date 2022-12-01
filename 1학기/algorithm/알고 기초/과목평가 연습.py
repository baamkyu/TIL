# 정렬 함수 만들기
# def sort_test(lst):
#     for _ in range(len(lst)):
#         for i in range(len(lst)-1):
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#     return lst
# sort_lst = [1,2,3,9,10,5,3,100,300,200,-5]
# print(sort_test(sort_lst))

# # 최대값 찾기
# def max_test(lst):
#     max_lst = lst[0]
#     for i in range(1, len(lst)):
#         if lst[i] > max_lst:
#             max_lst = lst[i]
#     return max_lst
#
# max_lst = [100,1000,50,500,30,300,3000,20,200]
# print(max_test(max_lst))
#
# def min_test(lst):
#     min_lst = lst[0]
#     for i in range(1, len(lst)):
#         if lst[i] < min_lst:
#             min_lst = lst[i]
#     return min_lst
#
# print(min_test(max_lst))

# # 카운팅 정렬
# arr = [3, 4, 5, 2, 2, 9, 8, 6]
# N = len(arr)
# sorted_arr = [0]*N
# c_arr = [0] * (max(arr) + 1)
# print(arr)
#
# #카운팅 - 값을 인덱스로 두고 해당 인덱스에 갯수 저장
# for i in arr:
#     c_arr[i] += 1
# print(c_arr)
#
# #누적 - 정렬된 리스트의 인덱스를 정해주기 위한 수 누적
# #가장 작은 수부터 인덱스 0을 부여, 이후 +1 됨
# for j in range(1, len(c_arr)):
#     c_arr[j] += c_arr[j-1]
# print(c_arr)
#
# #카운팅 값을 빼면서 정렬
# for k in range(N): # range(N-1, -1, -1) 가능
#     c_arr[arr[k]] -= 1 # 인덱스를 0부터 채우기 위
#     sorted_arr[c_arr[arr[k]]] = arr[k] # 존재하는 요소의 인덱스만 오른쪽부터 채움
# print(sorted_arr)

data = [list(input()) for _ in range(8)]
turn_data = zip(*data)
print(*data)
print(turn_data)