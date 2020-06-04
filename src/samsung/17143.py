R, C, m = map(int, input().split())
board = [[0]*C for _ in range(R)]
from collections import deque
import copy
# d
# 0 위
# 1 아래
# 2 오른쪽
# 3 왼쪽
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
remove_lst = []


def solve():
    shark = deque()
    result = 0
    flag = False
    for _ in range(m):
        r, c, s, d, z = map(int, input().split())
        r = r - 1
        c = c - 1
        d = d - 1
        shark.append([r, c, s, d, z])
        board[r][c] = z

    for j in range(C):  # 낚시왕이 오른쪽으로 한 칸 이동
        for i in range(R):  # 땅과 제일 가까운 상어를 잡는다.
            if board[i][j] != 0:
                for k in range(len(shark)):
                    y, x, _, _, z = shark[k]
                    if y == i and x == j:
                        del shark[k]
                        board[y][x] = 0

                        result += z
                        flag = True
                        break
            if flag == True:
                flag = False
                break

        # 이동
        for _ in range(len(shark)):
            y, x, s, d, z = shark.popleft()
            board[y][x] = 0
            for _ in range(s):  # 한 칸씩 이동
                ny = y + dy[d]
                nx = x + dx[d]
                if -1 < ny < R and -1 < nx < C:  # 범위 체크
                    y, x = ny, nx
                    continue
                else:  # 범위 밖이면 방향 바꿔줌
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    elif d == 3:
                        d = 2
                    ny = y + dy[d]
                    nx = x + dx[d]
                    y, x = ny, nx
            shark.append([y, x, s, d, z])

        # 좌표가 같은게 있으면 잡아먹기
        shark = deque(sorted(shark, key=lambda x:(x[0], x[1], x[4])))
        temp = deque()
        for i in range(len(shark)-1, -1, -1):
            y, x, s, d, z = shark[i]
            if i == len(shark)-1:
                board[y][x] = z
                temp.append([y, x, s, d, z])
                continue

            elif shark[i][0] == shark[i+1][0] and shark[i][1] == shark[i+1][1]:
                continue
            else:
                board[y][x] = z
                temp.append([y, x, s, d, z])

        shark = temp

    print(result)

solve()
