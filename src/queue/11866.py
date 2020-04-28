import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

deq = deque([i for i in range(1, n+1, 1)])
result = []
print('<', end='')

while len(deq) != 1:
    deq.rotate(-k)
    print(deq[-1], end=', ')
    result.append(deq[-1])
    deq.pop()
print(deq[0], end='')
print('>')
