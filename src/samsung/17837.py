from collections import deque
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = deque([list(map(int, input().split())) for _ in range(k)])
print('board', board)
print('move', move)


def move_right(y, x, direction):
    global move
    move.append([y, x + 1, direction])


def move_left(y, x, direction):
    global move
    move.append([y, x - 1, direction])


def move_up(y, x, direction):
    global move
    move.append([y - 1, x, direction])


def move_down(y, x, direction):
    global move
    move.append([y + 1, x, direction])


for i in range(1):
    if i == 1000:  # 턴이 1000번을 초과하는 경우 종료
        print(-1)
        break
    else:
        for _ in range(k):
            y, x, direction = move.popleft()
            if i == 0:
                y -= 1
                x -= 1

            if direction == 1:  # right
                if (x+1 >= n) or board[y][x+1] == 2:  # 벽이거나 파란색일 경우 방향 바꾸고 반대로 이동
                    direction = 2  # 방향만 바꿔주기
                    if board[y][x - 1] != 2:  # 반대에 파란색이 아니면
                        move_left(y, x, direction)
                    else:
                        move.append([y, x, direction])
                else:
                    move_right(y, x, direction)

            elif direction == 2:  # left
                if (x-1 < 0) or board[y][x-1] == 2:  # 벽이거나 파란색일 경우 방향 바꾸고 반대로 이동
                    direction = 1  # 방향만 바꿔주기
                    if board[y][x + 1] != 2:  # 반대에 파란색이 아니면
                        move_right(y, x, direction)
                    else:  # 반대에 파란색이면
                        move.append([y, x, direction])
                else:
                    move_left(y, x, direction)

            elif direction == 3:  # up
                if (y-1 < 0) or board[y-1][x] == 2:
                    direction = 4  # 방향만 바꿔주기
                    if board[y+1][x] != 2:  # 반대에 파란색이 아니면
                        move_down(y, x, direction)
                    else:  # 반대에도 파란색이면
                        move.append([y, x, direction])
                else:
                    move_up(y, x, direction)

            elif direction == 4:  # down
                if (y+1 >= n) or board[y+1][x] == 2:
                    direction = 3  # 방향만 바꿔주기
                    if board[y-1][x] != 2:  # 반대에 파란색이 아니면
                        move_up(y, x, direction)
                    else:  # 반대에도 파란색이면
                        move.append([y, x, direction])
                else:
                    move_down(y, x, direction)

        print(move)


