from collections import deque
N, M, V = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    y, x = map(int, input().split())
    adj[y][x] = 1
    adj[x][y] = 1


def dfs(v):
    result_dfs.append(v)
    visit[v] = 1
    for i in range(1, N+1):
        if adj[v][i] == 1 and visit[i] == 0:  # 연결 되어있고, 방문 하지 않았으면
            dfs(i)


def bfs(v):
    deq.append(v)
    visit[v] = 1
    while len(deq) != 0:
        # print(deq)

        for _ in range(len(deq)):
            v = deq.popleft()
            result_bfs.append(v)
            # visit[v]
            # print(v)

            for i in range(1, N+1):
                if adj[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    deq.append(i)


visit = [0] * (N+1)
result_dfs = []
dfs(V)
print(*result_dfs)

visit = [0] * (N+1)
result_bfs = []
deq = deque()
bfs(V)
print(*result_bfs)