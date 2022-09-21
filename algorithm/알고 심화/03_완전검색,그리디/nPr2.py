def f(i, k):
    if i == k:      # if 인덱스 i == 원소의 개수
        print(p)

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

N = 4
p = [i for i in range(1, N+1)]
f(0, N)     # 0번자리부터 시작, 원소의 개수는 3개

print(a)