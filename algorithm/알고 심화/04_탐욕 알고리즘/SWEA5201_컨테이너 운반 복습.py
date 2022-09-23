T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    weights.sort(reverse=True)  # 무거운 컨테이너가 앞으로 오도록 정렬
    trucks.sort(reverse=True)   # 많이 실을 수 있는 트럭이 앞으로 오도록 정렬

    now = [0] * M     # 현재까지 트럭이 실은 무게
    for weight in weights:              # 컨테이너 무게
        for i in range(len(trucks)):    # 트럭 번호 i
            if weight <= trucks[i]:
                if not now[i]:
                    now[i] = weight
                    break

    print(f'#{tc} {sum(now)}')