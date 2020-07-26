from collections import deque


def bfs(i, j):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    cnt = 1
    deq = deque()
    y, x = i, j
    visit[y][x] = 1
    deq.append([y, x])

    while len(deq) != 0:

        for _ in range(len(deq)):
            y, x = deq.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if -1 < ny < N and -1 < nx < M:
                    if board[ny][nx] == 1 and visit[ny][nx] == 0:
                        visit[ny][nx] = 1
                        deq.append([ny, nx])
                        cnt += 1
    return cnt


T = int(input())
all_cnts = []

for _ in range(T):
    M, N, K = map(int, input().split())
    visit = [[0]*M for _ in range(N)]
    board = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    cnts = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visit[i][j] == 0:
                cnt = bfs(i, j)
                cnts.append(cnt)

    all_cnts.append(len(cnts))

for i in range(T):
    print(all_cnts[i])

