from collections import deque
N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
deq = deque()
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(i, j):
    y, x = i-1, j-1
    deq.append([y, x])
    cnt = 1
    while deq:
        cnt += 1  # 한칸 더 (ny, nx)로 갈 거니까 미리 cnt
        for _ in range(len(deq)):
            y, x = deq.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if -1 < ny < N and -1 < nx < M:
                    if [ny, nx] == [N-1, M-1]:
                        return cnt

                    if board[ny][nx] == 1 and visit[ny][nx] == 0:
                        visit[ny][nx] = 1
                        deq.append([ny, nx])


cnt = bfs(1, 1)
print(cnt)
