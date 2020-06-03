'''
0 : 오른쪽
1 : 위쪽
2 : 왼쪽
3 : 아랫쪽
'''
board = [[0] * 101 for _ in range(101)]
n = int(input())
from collections import deque
curves = deque()
for _ in range(n):
    x, y, d, g = map(int, input().split())
    curves.append([x, y, d, g])


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for q in range(len(curves)):
    x, y, d, g = curves[q]
    board[y][x] = 1
    dir_list = deque([d])
    for j in range(g):
        for k in range(len(dir_list)-1, -1, -1):
            dir_list.append((dir_list[k]+1)%4)
    # print(dir_list)

    for i in dir_list:
        nx = x + dx[i]
        ny = y + dy[i]

        board[ny][nx] = 1
        x, y = nx, ny

    # for row in board:
    #     print(*row)
    # print()


def check_board(y, x):
    if board[y][x] == 1 and board[y][x+1] == 1 and\
        board[y+1][x] == 1 and board[y+1][x+1] == 1:
        return True
    return False


cnt = 0
for y in range(100):
    for x in range(100):
        if check_board(y, x) == True:
            cnt += 1

print(cnt)
