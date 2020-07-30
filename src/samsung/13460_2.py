from collections import deque
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visit = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# 방문 표시 꼭 할 것

# 종료 조건의 위치 - while deq: 아래에
# 부분 종료(Pruning)의 위치 - for i in range(4): 아래에
# move함수 안에, 'O'를 만날 경우 반환하는 좌표와 '#'을 만날 경우 반환하는 좌표가 다름에 유의
# 마지막에 print(-1)은 10번 이내의 경우에서 빨간 구슬과 파란 구슬이 동시에 빠지며 종료되는 경우를 생각하지 못해서 오래걸렸다.
# 방문 표시를 어디에서 해주어야 하는지에 대해
# 방문 표시를 deq.popleft() 이후에 하던, deq.append()이후에 하던 상관 없었다.
# nBy, nBx = Oy, Ox 는 가능하나
#  if nBy, nBx == Oy, Ox: 처럼 쓰면 안된다.  (대입 연산자는 가능, 비교는 안됨)


def move(y, x, i):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    while True:
        ny = y + dy[i]
        nx = x + dx[i]
        if board[ny][nx] == '#':
            return y, x, d
        elif board[ny][nx] == 'O':
            return ny, nx, d+1
        else:
            y = ny
            x = nx
            d += 1


def bfs():
    deq = deque()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    [Ry, Rx, By, Bx, Oy, Ox] = [0] * 6
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                Ry, Rx = i, j
                board[i][j] = '.'
            elif board[i][j] == 'B':
                By, Bx = i, j
                board[i][j] = '.'
            elif board[i][j] == 'O':
                Oy, Ox = i, j

    deq.append([Ry, Rx, By, Bx])
    visit[Ry][Rx][By][Bx] = 1
    cnt = 0
    while deq:
        cnt += 1
        if cnt > 10:  # 10번 이상 해도 탈출 할 수 없는 경우
            print(-1)
            return
        # print(deq)
        for _ in range(len(deq)):

            Ry, Rx, By, Bx = deq.popleft()
            visit[Ry][Rx][By][Bx] = 1

            for i in range(4):
                nRy, nRx, Rd = move(Ry, Rx, i)
                nBy, nBx, Bd = move(By, Bx, i)
                # 종료 조건
                if [nBy, nBx] == [Oy, Ox]:
                    continue

                if [nRy, nRx] == [Oy, Ox]:
                    print(cnt)
                    return

                if nRy == nBy and nRx == nBx:  # 두 구슬이 겹치면
                    if Rd > Bd:
                        nRy -= dy[i]
                        nRx -= dx[i]
                    else:
                        nBy -= dy[i]
                        nBx -= dx[i]

                if visit[nRy][nRx][nBy][nBx] == 0:
                    deq.append([nRy, nRx, nBy, nBx])

    print(-1)  # 10번 이내의 경우에서 빨간 구슬과 파란 구슬이 동시에 빠지며 종료되는 경우.


bfs()