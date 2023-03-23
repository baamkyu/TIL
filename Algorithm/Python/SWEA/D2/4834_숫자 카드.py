T = int(input())
for tc in range(1, T+1):
    n = int(input())
    input_num = int(input())
    change_input_num = [] # 입력받은 값을 리스트화해서 담을 빈 리스트
    max_num = 0           # 가장 많은 수
    many_num = 0          # 가장 많은 수의 개수
    for i in range(n):    # 입력받은 값을 리스트화
        change_input_num.append(input_num%10)
        input_num = input_num // 10

    # 카운팅 정렬
    arr = [0] * 10
    for j in change_input_num:
        arr[j] += 1
    many_num = max(arr)
    for k in range(9, -1, -1):  # 9부터 0까지 거꾸로 세면서, 최댓값과 일치하는 숫자를 출력
        if many_num == arr[k]:
            max_num = k
            break
    print(f'#{tc} {max_num} {many_num}')