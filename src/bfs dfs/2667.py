import sys
n = int(input())
visit = [[0] * n for i in range(n)]

graph = [list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]
cnt_list = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def dfs(x, y):
    global cnt
    visit[x][y] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 1 and visit[nx][ny] == 0:
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == 0:
            cnt = 0
            dfs(i, j)
            cnt_list.append(cnt)

print(len(cnt_list))
cnt_list.sort()
for i in cnt_list:
    print(i)

