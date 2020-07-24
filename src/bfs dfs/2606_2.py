from collections import deque
N = int(input())
M = int(input())

adj = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    y, x = map(int, input().split())
    adj[y][x] = 1
    adj[x][y] = 1


# def dfs(v):
#     visit[v] = 1
#     lst.append(v)
#     for i in range(N+1):
#         if adj[v][i] == 1 and visit[i] == 0:  # 연결되어 있고, 방문하지 않은 노드라면 go
#             dfs(i)
#
#
# visit = [0] * (N+1)
# lst = []
# V = 1  # 첫 번째로 방문할 노드
# dfs(V)
# print(len(lst)-1)  # 1번 컴퓨터와 연결된 컴퓨터 대수 출력
#


deq = deque()


def bfs(v):
    deq.append(v)
    visit[v] = 1
    while deq:
        for _ in range(len(deq)):
            v = deq.popleft()
            lst.append(v)

            for i in range(1, N+1):
                if adj[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    deq.append(i)


visit = [0] * (N+1)
lst = []
V = 1  # 첫 번째로 방문할 노드
bfs(V)
print(len(lst)-1)


