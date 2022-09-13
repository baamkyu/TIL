# # 부분집합 생성하기
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0]=i
#     for j in range(2):
#         bit[1]=j
#         for k in range(2):
#             bit[2]=k
#             for l in range(2):
#                 bit[3]=l
#                 print(bit)


# 비트 연산자를 통해 부분집합 생성하기
arr = [3,6,7,1,5,4]
n = len(arr)                        # n : 원소의 개수
for i in range(1<<n):               # 1<<n : 부분 집합의 개수(= 2**n)
    for j in range(n):              # 원수의 수만큼 비트를 비교
        if i & (1<<j):              # i의 j번 비트가 1인 경우
            print(arr[j], end=", ")  # j번 원소 출력
    print()
print()