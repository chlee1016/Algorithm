from collections import deque
from itertools import combinations
import copy


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
deq = deque()
virus_candd = deque()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
min_sec = 1000000


def check_board(board):
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:  # 하나라도 바이러스가 안퍼진 곳이 있으면 False 리턴
                return False
    return True


for y in range(n):
    for x in range(n):
        if board[y][x] == 2:
            virus_candd.append([y, x])


for viruses in combinations(virus_candd, m):
    # board, deq, 초기화
    board_candd = copy.deepcopy(board)
    flag_sec = 0
    sec = 0
    deq = deque()

    for y, x in virus_candd:
        if [y, x] in viruses:  # 활성 바이러스 표시
            board_candd[y][x] = 'v'
            deq.append([y, x])  # 활성 바이러스의 좌표 추가
        else:
            board_candd[y][x] = '*'  # 비활성 바이러스 표시

    for y in range(n):
        for x in range(n):
            if board_candd[y][x] == 1:  # 벽 표시
                board_candd[y][x] = '-'

    while len(deq) != 0:
        sec += 1

        for _ in range(len(deq)):
            y, x = deq.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if -1 < nx < n and -1 < ny < n and (board_candd[ny][nx] == 0 or board_candd[ny][nx] == '*'):
                    deq.append([ny, nx])
                    if board_candd[ny][nx] == '*':  # 테스트 케이스 7번 충족
                        board_candd[ny][nx] = 'v'

                    if board_candd[ny][nx] != '*' and board_candd[ny][nx] != 'v':
                        board_candd[ny][nx] = sec
                        flag_sec = sec  # 빈칸에 기록될 때만 저장, 최종 값이 저장 됨


    # for row in board_candd:
    #     print(*row)
    # print(flag_sec)
    # print()

    if check_board(board_candd) and flag_sec < min_sec:
        min_sec = flag_sec


if min_sec == 1000000:
    print(-1)
else:
    print(min_sec)