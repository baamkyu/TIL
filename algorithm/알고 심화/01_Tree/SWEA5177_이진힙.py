'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''

def heap_push(n):
    heap.append(n)  # 완전 이진트리니까 맨끝에 추가

    child = len(heap)-1
    parent = child // 2
    # 루트노드가 아니고, 위에 봤는데 더 큰 경우 계속 돎
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]  # swap
        child = parent
        parent = child // 2

def heap_push(n):
    heap.append(n)

    if heap[-1]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V_list = list(map(int,input().split()))

    heap = [0]           # 최소 힙을 위해 값을 가진 리스트 생성

    for node in V_list:  # 최소 힙
        heap_push(node)
    # print(heap)        # 최소 힙 출력

    hap = 0
    while (N//2) >= 1:
        hap += heap[N//2]
        N //= 2

    print(f'#{tc} {hap}')