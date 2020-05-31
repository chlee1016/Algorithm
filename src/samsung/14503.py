n, m = map(int, input().split())
ry, rx, rd = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
'''
# 0: 빈 칸 
# 1: 벽
# 2: 청소 한 곳
# d : 0 - 북, 1 - 동, 2 - 남, 3 - 서
'''

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def turn(d):
    if d > 0:
        return d-1
    else:
        return 3


def turn_back(d):
    if d > 1:
        return d-2
    else:
        return d+2


def solve():
    global ry, rx, rd
    y, x, d = ry, rx, rd
    # total_cnt = 0
    # total cnt를 쓰는게 아니라,
    # 그냥 board에서 2의 개수를 세니까 68 -> 57로 해결되었다.
    while True:
        # total_cnt += 1
        if board[y][x] == 0:
            board[y][x] = 2  # 현재 위치를 청소한다.

        # for row in board:
        #     print(*row)
        # print()

        turn_cnt = 0
        for _ in range(4):  # 2번 : 왼쪽방향부터 탐색 시작
            nd = turn(d)
            # print(nd)
            ny = y + dy[nd]
            nx = x + dx[nd]
            # print('y, x', y, x)
            # print('ny, nx', ny, nx)
            if board[ny][nx] == 0:  # 만약 청소할 공간이 있다면,
                # a 조건
                y, x, d = ny, nx, nd  # 업데이트
                break
            else:  # 만약 청소할 공간이 없다면,
                # b 조건
                turn_cnt += 1  # 청소할 공간이 없음을 카운트
                y, x, d = y, x, nd  # 그 방향으로 회전만 한다.
                continue  # 2번으로 돌아간다.

        if turn_cnt == 4:
            if board[y + dy[turn_back(d)]][x + dx[turn_back(d)]] == 1:
                # d 조건
                # 네 방향 모두 청소가 이미 되어있거나 벽이면서,
                # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춤
                # print(total_cnt)
                break
            else:
                # c 조건
                # 네 방향 모두 청소가 이미 되어 있는 경우
                y = y + dy[turn_back(d)]  # 뒤로 한 칸 후진
                x = x + dx[turn_back(d)]
                # 바라보는 방향 유지

    print(sum(board, []).count(2))
    return

solve()






