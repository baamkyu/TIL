# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

T = int(input())
for tc in range(T):
    k = int(input())  # k층
    n = int(input())  # n호
    people = [i for i in range(1, n+1)]   # 0층
    # 찾으려는 층, 호까지 계속 계산 반복문
    for i in range(1, k+1):
        for j in range(1, n):
            people[j] += people[j-1]
    print(people[n-1])

