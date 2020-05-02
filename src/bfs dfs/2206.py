# 벽을 하나씩 부수고 매 경우마다 bfs를 수행하면 시간 초과
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    que = deque()
    que.append([1, 0, 0])
    visit = [[[0] * m for _ in range(n)] for _ in range(2)]
    visit[1][0][0] = 1
    while len(que) != 0:
        w, y, x = que.popleft()

        if x == m - 1 and y == n - 1:
            return visit[w][y][x]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < m) and (0 <= ny < n):
                # 벽이고 벽을 뚫을 수 있는 상태이면
                if graph[ny][nx] == 1 and w == 1:
                    # 벽을 뚫은 곳에다 count하고,
                    visit[0][ny][nx] = visit[1][y][x] + 1
                    # 벽 뚫은 상태에서 탐색할 수 있도록 큐에 저장
                    que.append([0, ny, nx])
                # 벽이 아니고 방문하지 않았다면
                elif graph[ny][nx] == 0 and visit[w][ny][nx] == 0:
                    # count를 이어나감
                    visit[w][ny][nx] = visit[w][y][x] + 1
                    que.append([w, ny, nx])
    return -1


print(bfs())


