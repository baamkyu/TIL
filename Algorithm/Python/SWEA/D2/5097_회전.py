T = int(input())
for tc in range(1, T+1):
    size, turn = map(int, input().split())
    num_list = list(map(int, input().split()))
    for _ in range(turn):
        pop = num_list.pop(0)
        num_list.append(pop)
    print(f'#{tc} {num_list[0]}')