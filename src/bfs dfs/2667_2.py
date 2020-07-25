N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
visit = [[0]*N for _ in range(N)]


def dfs(y, x):
    global cnt
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if -1 < nx < N and -1 < ny < N:
            if board[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                cnt += 1
                dfs(ny, nx)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
total_cnt = 0
cnts = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            cnt = 1
            dfs(i, j)
            cnts.append(cnt)
            total_cnt += 1

print(total_cnt)
for ele in cnts:
    print(ele)




