import sys
n = int(input())
m = int(input())
stack = []


def dfs(v):
    # print(v, end=' ')
    visit[v] = 1
    stack.append(v)
    for i in range(1 , n + 1):
        if visit[i] == 0 and adj[v][i] == 1:
            dfs(i)


adj = [[0] * (n+1) for i in range(0,n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adj[x][y] = 1
    adj[y][x] = 1

visit = [0 for i in range(0, n+1)]
dfs(1)
print(len(stack)-1)

