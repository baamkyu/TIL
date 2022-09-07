import sys
sys.stdin = open('list2_부분집합의 합.txt', 'r')
T = int(input())
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(T):
    N, K = map(int, input().split()) # N : 원소의 개수, K : 원소들의 합
    count = 0
    for i in range(1<<len(arr)): # 모든 부분집합의 개수
        length = 0
        sub_list = []
        for j in range(len(arr)): # 원소의 길이
            if i & (1<<j): # j번째 인덱스
                sub_list.append(arr[j])
                length+=1
        if length==N:
            sum_list = 0
            for k in range(length):
                sum_list += sub_list[k]

            if sum_list==K:
                count+=1
    print(f'#{tc+1} {count}')









# # T = int(input())
# arr = [1,2,3,4,5,6,7,8,9,10,11,12]
# # for tc in T:
#     # N, K = map(int, input().split()) # N : 원소의 개수, K : 원소들의 합
# for i in range(1<<len(arr)): # 모든 부분집합의 개수
#     for j in range(len(arr)): # 원소의 길이
#         if i & (1<<j): # j번째 인덱스
#             print(arr[j], end = ", ")
#         else:
#             print(' ', end = ", ")
#     print()
# print()