from collections import deque

import sys
n = int(input())
deq = deque()
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        deq.append(command[1])
    elif command[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])

# list로 선언해서 pop(0)를 하게 되면,
# 첫 번째 element를 pop 하고나서 나머지 element들의 인덱스를
# 1칸씩 당기는 과정에서 O(n)의 계산량이 발생한다.
# 따라서 deque를 이용한다.