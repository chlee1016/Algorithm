from collections import deque
n, k = map(int, input().split())
MAX = 100001
graph = [0] * MAX


def bfs():
    que = deque()
    que.append(n)
    while len(que) != 0:
        x = que.popleft()
        if x == k:
            return graph[x]

        for nx in [x+1, x-1, 2*x]:
            if (0 <= nx < MAX) and (graph[nx] == 0):
                que.append(nx)
                graph[nx] = graph[x] + 1


print(bfs())

# graph = [0] * 100000  # 범위 조심, 테스트 케이스는 모든 범위를 체크함

# seconds라는 변수를 새로 선언할 경우, 메모리 초과가 뜸

# graph[k] = 1 이게 조건을 방해하는 것 같다.

# 종료조건을 다음과 같이 바꿀 경우, 오답이 나옴
# elif (0 <= nx < MAX) and graph[nx] == 1:
#     return graph[x] + 2
