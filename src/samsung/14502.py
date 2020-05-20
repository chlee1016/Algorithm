import sys
# sys.setrecursionlimit(10000)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


max_count = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 벽 세개를 세우는 경우를 탐색하는 함수 출력
def wall(cnt):
    if cnt == 3:  # 종료 조건
        bfs()
        return
    else:  # 벽이 세개가 아닌 경우, 추가로 벽을 세워야 함
        for y in range(n):
            for x in range(m):
                if board[y][x] == 0:
                    board[y][x] = 1  # 벽을 세우고
                    wall(cnt+1)  # 함수 재호출
                    board[y][x] = 0


from collections import deque
import copy
def bfs():  # 바이러스를 퍼뜨리게 하는 함수
    global max_count

    # temp_board = board 와 다름
    temp_board = copy.deepcopy(board)

    count = 0
    que = deque()
    for y in range(n):
        for x in range(m):
            if temp_board[y][x] == 2:  # 바이러스가 있는 위치 추가
                que.append([y, x])

    while len(que) != 0:
        y, x = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < m and -1 < ny < n:
                if temp_board[ny][nx] == 0:
                    temp_board[ny][nx] = 2
                    que.append([ny, nx])

    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 0:
                count += 1

    max_count = max(count, max_count)


wall(0)
print(max_count)
