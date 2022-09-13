# # 데이터가 많아질수록 큐.py 에 비해 느려짐
# q = []
#
# q.append(10)
# q.append(20)
# q.append(30)
#
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))


# 속도 문제가 해결되긴 하는데 import 지양하자.
from collections import deque
q = deque()

q.append(10)
q.append(20)
q.append(30)

print(q.popleft())
print(q.popleft())
print(q.popleft())
