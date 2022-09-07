# N = 3
# q = [0] * N
# front = -1
# rear = -1
#
# rear += 1   # enqueue(10)
# q[rear] = 10
#
# rear += 1   # enqueue(20)
# q[rear] = 20
#
# rear += 1   # enqueue(30)
# q[rear] = 30
#
# front += 1  # dequeue()
# print(q[front])
#
# front += 1  # dequeue()
# print(q[front])
#
# front += 1  # dequeue()
# print(q[front])
#
# print(q)




N = 3
q = [0] * N
front = -1
rear = -1

rear = (rear + 1) % N   # enqueue(10)
q[rear] = 10

rear = (rear + 1) % N   # enqueue(20)
q[rear] = 20

rear = (rear + 1) % N   # enqueue(30)
q[rear] = 30

front = (front + 1) % N  # dequeue()
print(q[front])

front = (front + 1) % N  # dequeue()
print(q[front])

front = (front + 1) % N  # dequeue()
print(q[front])

print(q)