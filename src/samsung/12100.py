from collections import deque
from copy import deepcopy
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def rotate(row, n):
    return row[-n:] + row[:-n]


def func_2048(board, dir):
    for i in range(N):  # 모든 행에 대해서
        # 1. 해당 방향으로 밀착시키기
        cnt_zero = 0
        for j in range(N-1, -1, -1):
            if board[i][j] == 0:
                cnt_zero += 1
            else:
                if cnt_zero != 0 :
                    rotate(board[i], ((-1)**(dir%2))*cnt_zero)
                    cnt_zero = 0

        # 2. 1) 같은 숫자를 검사하고, 합치기
        for j in range(N-2, -1, -1):
            if board[i][j] == 0:
                continue
            elif board[i][j] == board[i][j+1]:
                board[i][j+1] = 2*board[i][j+1]
                board[i][j] = 0

        print(board[i])
        # 2. 2) 숫자를 당겨서 0으로 대체된 공간을 없애기
        cnt_zero = 0
        for j in range(N - 1, -1, -1):
            if board[i][j] == 0:
                cnt_zero += 1
            else:
                if cnt_zero != 0:
                    print(board[i])

                    board[i] = rotate(board[i], ((-1) ** (dir % 2)) * cnt_zero)
                    print(board[i])
                    cnt_zero = 0
    return board


def bfs(board):
    deq = deque()
    deq.append(board)
    max_values = []
    cnt = 0

    while deq:
        cnt += 1
        if cnt == 5:
            max_value = -1
            for i in range(N):
                for j in range(N):
                    max_value = max(max_value, board[i][j])
            max_values.append(max_value)

        for _ in range(len(deq)):
            board = deq.popleft()
            for i in range(4):
                temp_board = deepcopy(board)
                temp_board = func_2048(temp_board, i)
                deq.append(temp_board)

    return max(max_values)

print(board)
board = func_2048(board, 0)
print(board)