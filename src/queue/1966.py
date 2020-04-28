import sys
from collections import deque
T = int(input())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    priority_id = deque([i for i in range(0, N)])
    deq = deque(priority)
    count = 0
    while len(deq) != 0:
        if deq[0] == max(deq):
            count += 1
            if deq[0] == priority[M] and priority_id[0] == M:
                print(count)
            deq.popleft()
            priority_id.popleft()

            # print('priority[0]', priority[0])
            # print('deq[0]', deq[0])

        else:
            deq.rotate(-1)
            priority_id.rotate(-1)




