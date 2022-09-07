
#
# # 열 우선 순회
# for j in range(m):
#     for i in range(n):
#         print(arr[i][j])
#
# # 지그재그 순회
# for i in range(n):
#     for j in range(m):
#         arr[i][j + (m-1-2*j) * (i%2)] # 1 2 3 4 8 7 6 5 9 10 11 12
#                                       # 행 번호가 짝수면 i%2에서 [i][j]로 된다.
#                                       # 행 번호가 홀수인 경우에 [i][j+(m-1-2*j)]
#
#

#

#
#
#

#
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
#
#
# # 비트 연산자를 통해 부분집합 생성하기
# arr = [3,6,7,1,5,4]
# n = len(arr)                        # n : 원소의 개수
# for i in range(1<<n):               # 1<<n : 부분 집합의 개수(2**n)
#     for j in range(n):              # 원수의 수만큼 비트를 비교
#         if i & (1<<j):              # i의 ㅓ번 비트가 1인 경우
#             print(arr[j], end=", ")  # j번 원소 출력
#         print()
#     print()
#
# # 원하는 값을 가진 인덱스를 찾는 함수 (없는 경우 -1출력)
# def search(arr, key, N): #arr: 배열, key: 원하는 값, N: 배열의 길이
#     for i in range(0, N-1):
#         if arr[i]==key:
#             return i
#     return -1
#
# # 이진 검색 알고리즘
# def binarySearch(a,N,key):
#     start = 0
#     end = N-1
#     while start<=end :      # start가 end를 넘어가는건 검색 실패를 의미
#         middle = (start+end)//2
#         if a[middle]==key : #검색 성공
#             return true
#         elif a[middle]>key :
#             end = middle -1
#         else:
#             start = middle+1
#     return false            #검색 실패
#
# # 선택 정렬
# def selectionSort(arr,N):
#     for i in range(N-1): #구간 시작
#         minIdx = i #기준 위치
#         for j in range(i+1, N):
#             if arr[minIdx] > arr[j]:
#                 minIdx = j
#         arr[i], arr[minIdx] = arr[minIdx], arr[i]
#
# # 선택 정렬2
# arr = [7,2,5,3,4,1]
# N = len(arr)
#
# for i in range(N-1):
#     minIdx = i #구간의 맨 앞을 최소값으로 가정
#     for j in range(i+1, N): # 실제 최소값 인덱스 찾기
#         if arr[minIdx]>arr[j]:
#             minIdx=j
#     arr[minIdx], arr[i] = arr[i], arr[minIdx] # 최소값을 구간 맨 앞으로
# print(arr)
#
#
#
#
# # 복습
# N = 3 #행
# M = 4 #열
# # N개의 원소를 갖는 0으로 초기화된 1차원 배열
# arr1 = [0]*N
# print(arr1)
#
# # 크기가 N*M이고 0으로 초기화된 2차원 배열
# arr2 = [[0]*M for _ in range(N)]
# print(arr2)
#
# arr3 = [[0]*M]*N #안 되는 코드!!
# print(arr3)
# arr3[0][0] = 1
# print(arr3) # 주소까지 복사되어서 안 됨!!
#
# # N*M 행렬을 입력하고 모든 원소들의 합 구하기
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# hap = 0
# for i in range(N):
#     for j in range(M):
#         hap += arr[i][j]
# print(hap)
#
# # 각 항의 합을 구하고 그 중 최대값을 출력하시오.
# # 3
# # 1 2 3
# # 4 5 6
# # 7 8 9
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# maxV = 0 # 최대 행의 합
# for i in range(N):
#     rowhap = 0  # 행의 합
#     for j in range(N): # i행의 j열에 접근
#         rowhap += arr[i][j]
#     if maxV < rowhap:
#         maxV = rowhap
# print(maxV)
#
# # 대각선의 합
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# hap = 0
# for i in range(N):
#     hap+=arr[i][i]
#
# # 양 대각선의 합
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# hap = 0
# for i in range(N):
#     hap += arr[i][i]
# for i in range(N):
#     hap+=arr[i][N-1-i]
# print(hap)
# if N % 2 == 1:
#     hap -= arr[N//2][N//2]
# print(hap)

# # 대각선 양쪽 합
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# hap_under = 0
# hap_over = 0
# for i in range(N):
#     for j in range(N):
#         if i > j:
#             hap_under+=arr[i][j]
#         elif j > i:
#             hap_over+=arr[i][j]
#
# if hap_under > hap_over:
#     print(hap_under)
# else:
#     print(hap_over)