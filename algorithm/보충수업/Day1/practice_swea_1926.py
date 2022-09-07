# N = int(input())
# lst = []
# for i in range(1, N+1):
#     if i % 3 != 0:
#         lst.append(i)
#     else:
#         lst.append("-")
# print(lst)
for j in range(1, N+1):
    N = list(map(int,input()))
    lst=[]
    for i in range(len(N)):
        print(N, i)
        if N[i] == 3 or N[i] == 6 or N[i] == 9:
            lst.append('-')
        else:
            lst.append(int(i))
    print(lst)
