import sys
sys.stdin = open('list2_특별한정렬.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    temp_lst = []
    for i in range(N-1, 0, -1):  # 버블 정렬
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    for k in range(len(lst)//2):  # for문당 2개씩 넣기 때문에 len//2 해서 for문 진행
        temp_lst.append(lst[N-k-1])
        temp_lst.append(lst[k])
        temp_lst2 = temp_lst[0:10]  # 10개만 출력하기 위함
    print(f'#{tc}',*temp_lst2)  # f스트링과 *를 같이 쓰는 방법 !! 꼭 알자!!

