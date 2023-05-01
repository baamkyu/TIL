for _ in range(10):
    tc = int(input())
    queue = list(map(int, input().split()))

    number = 1  # 뺄 수

    while True:
        queue.append(queue.pop(0) - number)
        number += 1

        if number == 6:  # 1~5가 한 싸이클이므로 6이 되면 다시 1로 돌아간다 
            number = 1

        if queue[-1] <= 0:  # 마지막 수가 0보다 작아지면 0을 유지
            queue[-1] = 0
            break
    result = ' '.join(map(str, queue))
    print(f'#{tc} {result}')
