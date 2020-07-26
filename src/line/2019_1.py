from collections import deque
C, B = map(int, input().split())
def bfs(C, B):
    interval = 0
    sec = 0
    deq = deque()
    deq.append(B)
    while len(deq) != 0:
        sec += 1
        interval += 1
        C = C + interval
        print('C', C)
        if not (-1 < C < 200001):
            print(-1)
            return

        for _ in range(len(deq)):
            B = deq.popleft()

            NB = B - 1
            if -1 < NB < 200001:
                if NB != C:
                    deq.append(NB)
                else:
                    print(sec)
                    return

            NB = B + 1
            if -1 < NB < 200001:
                if NB != C:
                    deq.append(NB)
                else:
                    print(sec)
                    return

            NB = B * 2
            if -1 < NB < 200001:
                if NB != C:
                    deq.append(NB)
                else:
                    print(sec)
                    return


bfs(C, B)