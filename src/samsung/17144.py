from collections import deque
r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
add_board = [[0]*c for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    deq = deque()
    air_clear = deque()
    sec = 0
    for y in range(r):
        for x in range(c):
            if board[y][x] > 0:
                deq.append([y, x])
            elif board[y][x] == -1:
                air_clear.append([y, x])

    while len(deq) != 0:

        sec += 1
        for _ in range(len(deq)):
            y, x = deq.popleft()
            cnt = 0
            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]

                if -1 < nx < c and -1 < ny < r and board[ny][nx] != -1:
                    # 확산이 가능하면

                    deq.append([ny, nx])

                    add_board[ny][nx] = add_board[ny][nx] + int(board[y][x] / 5)
                    cnt += 1  # 확산된 방향 개수 표시

            add_board[y][x] = add_board[y][x] - int(board[y][x] / 5) * cnt # 줄이고

        for y in range(r):
            for x in range(c):
                board[y][x] = board[y][x] + add_board[y][x]  # 더하고

        # print('board')
        # for row in board:
        #     print(*row)
        # print()



        ## 공기청정기 작동
        air_clear = deque(sorted(air_clear))
        print('공기청정기 작동 1')

        air_y, air_x = air_clear[0]
        for y in range(air_y, 0, -1):  # 아래로
            if y == air_y:
                continue
            else:
                board[y][0] = board[y-1][0]
        for x in range(c-1):  # 우측으로 가면서 좌측으로
            board[0][x] = board[0][x+1]
        for y in range(air_y):  # 위로
            board[y][c-1] = board[y+1][c-1]
        for x in range(c-1, -1, -1):  # 좌측으로 가면서 우측으로 이동
            if x == 0:
                board[air_y][x+1] = 0
            else:
                board[air_y][x] = board[air_y][x-1]



        # for row in board:
        #     print(*row)
        # print()


        print('공기청정기 작동 2')

        air_y, air_x = air_clear[1]
        for y in range(air_y, r-1):
            if y == air_y:
                continue
            else:
                board[y][0] = board[y+1][0]

        for x in range(c-1):
            board[r-1][x] = board[r-1][x+1]

        for y in range(r-1, air_y, -1):  # 범위에 -1을 안써주면 for문 통과 안함
            board[y][c-1] = board[y-1][c-1]

        for x in range(c-1, 0, -1):
            if x == 1:
                board[air_y][x] = 0
            else:
                board[air_y][x] = board[air_y][x-1]

        # for row in board:
        #     print(*row)
        # print()


        deq = deque()  # 공기 청정기 움직임 반영된 것을 토대로 초기화
        for y in range(r):
            for x in range(c):
                add_board[y][x] = 0  # add_board의 초기화 깜빡해서 오답이 나옴
                if board[y][x] > 0:
                    deq.append([y, x])

        if sec == t:
            break


bfs()
total_dust = 0
for y in range(r):
    for x in range(c):
        if board[y][x] == -1:
            continue
        else:
            total_dust += board[y][x]
# print(board)
print(total_dust)

