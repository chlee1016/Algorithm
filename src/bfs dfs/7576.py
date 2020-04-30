import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
que = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    days = -1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                que.append([i, j])

    while len(que) != 0:
        # 모든 토마토가 익은 상태이면 days = 0이 됨
        days += 1
        # 하루를 기준으로 append와 pop이 일어남.
        for _ in range(len(que)):
            y, x = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                elif graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    # graph[ny][nx] = 1  # 이것도 됨
                    que.append([ny, nx])

    # 모든 토마토가 익을 수는 없는 상태이면 -1
    for a in graph:
        if 0 in a:
            return -1
    return days  # 모든 토마토가 익을 때까지의 최소 날짜 반환

print(bfs())



