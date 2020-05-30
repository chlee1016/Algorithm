'''
. : 빈칸
# : 벽
o : 구멍의 위치
R : 빨간 구슬 위치
B : 파란 구슬 위치
'''
# https://jeongchul.tistory.com/666
# 기울이기 : 상 하 좌 우
# 공은 동시에 움직임
# 빨간 구슬이 구멍에 빠지면 성공
# 파란 구슬이 구멍에 빠지면 실패
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지
from collections import deque
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
# visit [n][m][n][m]
visit = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
deq = deque()
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def move(y, x, dy, dx):
    count = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':  # 요 부분 에러 조심, 미래 좌표를 가지고 체크할 필요
        y += dy
        x += dx
        count += 1
    return y, x, count


def bfs():
    ry, rx, by, bx = 0, 0, 0, 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'R':
                ry, rx = y, x

            elif board[y][x] == 'B':
                by, bx = y, x

    deq.append([ry, rx, by, bx])
    visit[ry][rx][by][bx] = 1

    cnt = 0
    while True:
        cnt += 1
        if cnt > 10:
            print(-1)
            return

        for _ in range(len(deq)):
            ry, rx, by, bx = deq.popleft()
            for i in range(4):
                nry, nrx, r_dist = move(ry, rx, dy[i], dx[i])
                nby, nbx, b_dist = move(by, bx, dy[i], dx[i])

                if board[nby][nbx] == 'O':  # 파란 구슬이 빠진 경우 그 경로 제외
                    continue
                if board[nry][nrx] == 'O':  # 빨간 구슬이 빠진 경우 게임 종료
                    print(cnt)
                    return
                if nry == nby and nrx == nbx:  # 빨간 구슬과 파란 구슬이 동시에 빠질 경우
                    if r_dist > b_dist:  # 이동 거리는 두 구슬이 같아야 하므로 위치 조정
                        nry -= dy[i]
                        nrx -= dx[i]
                    else:
                        nby -= dy[i]
                        nbx -= dx[i]

                if visit[nry][nrx][nby][nbx] == 0:
                    deq.append([nry, nrx, nby, nbx])
                    visit[nry][nrx][nby][nbx] = 1


bfs()
