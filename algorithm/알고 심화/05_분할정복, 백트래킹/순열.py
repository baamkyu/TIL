# order[] : 순열의 순서를 저장하는 리스트
def per(order, k, n):
    if k == n:
        print(order)
    else:
        check = [0] * n
        for i in range(k):
            check[order[i]] = 1
        for i in range(n):
            if check[i] == 0:
                order[k] = i
                per(order, k+1, n)

order = [1,2,3,4]
print(per(order, 1, 4))
