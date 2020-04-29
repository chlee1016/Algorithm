import sys
sys.setrecursionlimit(50000)

def dfs(x, y):
    global cnt
    visit[y][x] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if graph[ny][nx] == 1 and visit[ny][nx] == 0:
            dfs(nx, ny)


T = int(input())
for _ in range(T):
    cnt_list = []

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    print(visit)
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and visit[y][x] == 0:
                cnt = 0
                dfs(x, y)
                cnt_list.append(cnt)

    print(len(cnt_list))


