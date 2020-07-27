from collections import deque


def bfs(board):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    deq = deque()

    sum_board = 0
    for row in board:
        sum_board += sum(row)

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                deq.append([i, j])

    day = -1

    while deq:
        day += 1
        for _ in range(len(deq)):
            y, x = deq.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if -1 < ny < N and -1 < nx < M:
                    if board[ny][nx] == 0:
                        board[ny][nx] = 1
                        deq.append([ny, nx])

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:  # 토마토가 모두 익지는 못하는 상태
                return -1

    return day


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]




if sum_board == M * N:  # 저장 될 때부터 모든 토마토가 익어있는 상태
    print(0)
else:
    result = bfs(board)
    print(result)