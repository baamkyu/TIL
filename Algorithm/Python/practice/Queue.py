# 세개의 데이터 1,2,3을 차례롤 큐에 삽입하고
# 큐에서 세개의 데이터를 차례로 꺼내서 출력한다
# 1, 2, 3이 출력 되어야 함

def enqueue(list, item):
    list.append(item)

def dequeue(list):
    pop = list.pop(0)
    return pop

queue = []
enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)

while queue:
    print(dequeue(queue))
    