# 버리고 옮기고
# rotate의 방향 -1은 왼쪽, +1은 오른쪽
from collections import deque

n = int(input())
deq = deque([i for i in range(1, n+1)])

for i in range(n):
    if len(deq) != 1:
        deq.popleft()
        deq.rotate(-1)
    else:
        print(deq[0])


