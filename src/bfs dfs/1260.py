# 그래프를 DFS로 탐색한 결과(방문 기록)와 BFS로 탐색한 결과를 출력하는
# 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는
# 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이
# 없는 경우 종료한다. 정점 번호는 1번부터 N번 까지이다.
# N M V
# 정점(꼭지점)의 개수, 간선(선분)의 개수, 탐색을 시작할 정점의 번호
# 다음 M개 줄에는 간선이 연결하는 두 정점의 번호가 주어짐
# DFS : stack = 재귀(시스템 내부적으로 stack을 사용하는 형태)
# 1. 스택의 최상단 노드를 확인한다.
# 2. 방문하지 않은 인접 노드가 있으면 스택에 넣고 방문처리한다.
# 3. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 뺀다.
# BFS : queue
# 1. 큐에서 하나의 노드를 꺼낸다.
# 2. 해당 노드에 연결된 노드 중 방문하지 않은 노드를 방문하고,
# 차례대로 큐에 삽입한다.
import sys
from collections import deque
n, m, v = list(map(int, sys.stdin.readline().split()))
que = deque()


def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and adj[v][i] == 1:
            dfs(i)


def bfs(v):
    # 첫 번째 노드가 큐에 들어가 있는 상태에서 시작
    que.append(v)
    visit[v] = 1

    while len(que) != 0:
        v = que[0]
        que.popleft()  # 큐에서 데이터를 하나 꺼내고
        # 큐의 길이가 0이면 종료
        print(v, end=' ')  # 출력

        # 연결 노드들을 추가하고, 방문표시
        for i in range(1, n + 1):
            if visit[i] == 0 and adj[v][i] == 1:
                que.append(i)
                visit[i] = 1




adj = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adj[x][y] = 1
    adj[y][x] = 1
visit = [0 for i in range(n + 1)]
dfs(v)
print()
visit = [0 for i in range(n + 1)]
bfs(v)

