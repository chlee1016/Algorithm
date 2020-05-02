from collections import deque

m, n, h = map(int, input().split())

dx = [0, 0, -1, 0, 1, 0]
dy = [0, 0, 0, 1, 0, -1]
dz = [1, -1, 0, 0, 0, 0]
que = deque()
graph = [[list(map(int, list(input().split()))) for i in range(n)] for j in range(h)]


def bfs():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    que.append([i, j, k])

    days = -1

    while len(que) != 0:
        days += 1
        for _ in range(len(que)):
            z, y, x = que.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if (0 <= nx < m) and (0 <= ny < n) and (0 <= nz < h):
                    if graph[nz][ny][nx] == 0:
                        que.append([nz, ny, nx])
                        graph[nz][ny][nx] = graph[z][y][x] + 1
    for plane in graph:
        for vector in plane:
            if 0 in vector:
                return -1
    return days


print(bfs())

