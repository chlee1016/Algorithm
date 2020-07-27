from collections import deque


def bfs(board):
    dz = [0, 0, 0, 0, 1, -1]
    dy = [-1, 0, 1, 0, 0, 0]
    dx = [0, -1, 0, 1, 0, 0]
    deq = deque()

    sum_board = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                sum_board += board[k][i][j]
                if board[k][i][j] == 1:
                    deq.append([k, i, j])

    if sum_board == M * N * H:  # 저장 될 때부터 모든 토마토가 익어있는 상태
        return 0
    day = -1

    while deq:
        day += 1
        for _ in range(len(deq)):
            z, y, x = deq.popleft()
            for i in range(6):
                nz = z + dz[i]
                ny = y + dy[i]
                nx = x + dx[i]
                if -1 < nz < H and -1 < ny < N and -1 < nx < M:
                    if board[nz][ny][nx] == 0:
                        board[nz][ny][nx] = 1
                        deq.append([nz, ny, nx])

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if board[k][i][j] == 0:  # 토마토가 모두 익지는 못하는 상태
                    return -1

    return day


M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(bfs(board))
