T = int(input())
for tc in range(1, T+1):
    N = int(input())
    queue = [] 
    for i in range(N):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(queue[i-1][j-1] + queue[i-1][j])
        queue.append(temp)
    print(f'#{tc }')
    for i in range(N):
      print(' '.join(map(str, queue[i])))