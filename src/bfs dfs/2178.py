# 첫 번째 노드가 큐에 들어가 있는 상태에서 시작
# 큐에서 데이터를 하나 꺼내고
# 큐의 길이가 0이면 종료
# 연결 노드들을 추가하고, 방문표시
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip()))for i in range(n)]
visit = [[0] * m for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
que = deque()


def bfs(x, y):
    visit[y][x] = 1
    # 탐색할 노드를 큐에 추가
    que.append([y, x])
    while len(que) != 0:
        y, x = que[0]
        # print(que)
        que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표 안에 나타나 있지 않으면 통과
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            # 방문하지 않은 연결 점이 있으면 방문
            if graph[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = visit[y][x] + 1
                que.append([ny, nx])
                # print('자식노드추가')
                if nx == m - 1 and ny == n - 1:
                    print(visit[ny][nx])


bfs(0, 0)
