# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 것을 고르시오.

def powerset(n, hap):
    if hap > 10:
        return
    if n == 10:
        if hap == 10:
            temp = []
            for i in range(10):
                if check[i]:
                    temp.append(arr[i])
            result.append(temp)
        return
    
    check[n] = 0
    powerset(n+1, hap)
    check[n] = 1
    powerset(n+1, hap + arr[n])

arr = list(range(1, 11))
check = [0] * 10
result = []

powerset(0, 0)
print(result)