from collections import deque
from copy import deepcopy


def rotate_90(board):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N-1-i] = board[i][j]
    return temp


def rotate_270(board):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[N-1-j][i] = board[i][j]
    return temp


def move(board, dir):
    # print('1', board)
    temp_board = []
    for i in range(N):
        # 2 0 2 2 0 2
        # <-
        # 2 2 2 2 2 0
        # 0 4 0 4 2 0
        # 4 4 2 0 0 0
        # 0, 1, 2, 3  : 우 좌 상 하

        temp_lst = []
        for j in range(N):
            if board[i][j] != 0:
                temp_lst.append(board[i][j])  # 0이 아닌 요소들을 lst에 추가
        if dir % 2 == 0:
            temp_lst = [0] * (N-len(temp_lst)) + temp_lst  # 나머지 요소들을 좌측에 0으로 패딩
        else:
            temp_lst = temp_lst + [0] * (N - len(temp_lst))   # 나머지 요소들을 우측에 0으로 패딩
        temp_board.append(temp_lst)



    # print('2', temp_board)
    return temp_board


def func_2048(board, dir):
    # 1. 해당 방향으로 밀착시키기
    # print('1', board)
    if dir > 1:
        board = rotate_90(board)

    board = move(board, dir)
    # print('2', board)

    # 2. 1) 같은 숫자를 검사하고, 합치기

    # 오류가 났었던 이유 1. 좌측 이동, 하단 이동의 경우 왼쪽부터 검사해야 함.
    # for j in range(N-1) 이어야 한다. (for j in range(N-2, -1, -1)이면 안됨)
    # 좌측 이동을 예로, 오른쪽 부터 검사(range(N-2, -1, -1))하는 경우,
    # 8 8 8 8 8 8 4 4 4 -> 16 16 16 4 8 0 0 0 0이 되므로, 오답
    # 따라서, 좌측 이동과 하단 이동 그리고 우측 이동과 상단 이동을 분리하고
    # j가 관여되는 for문의 검색 시작점을 반대로 설정해 줌

    # 오류가 났었던 이유 2.
    # 좌측 이동 또는 하단 이동에서 같은 숫자를 찾아 2배 해주는 과정에서
    # board[i][j+1] = 2*board[i][j+1]  (X)
    # board[i][j] = 0
    #
    # board[i][j] = 2*board[i][j]      (O)
    # board[i][j+1] = 0
    # ex) 좌측 이동시 8 8 16 8 0 0 0을 테스트할 경우,
    # 처음 8 두개가 합쳐져서 0 16 16 8 0 0 0가 되고,
    # 이는 다시 0 0 32 8 0 0 0이 되므로, 합쳐진 것이 또 합쳐지는 결과가 생긴다.
    # 따라서, board[i][j]를 2배하고, 진행 방향에 있는 board[i][j+1] = 0을 취한다.
    for i in range(N):
        if dir % 2 == 1:  # 좌, 하
            for j in range(N-1):
                if board[i][j] == 0:
                    continue
                elif board[i][j] == board[i][j + 1]:
                    board[i][j] = 2 * board[i][j]
                    board[i][j+1] = 0
        else:  # 우, 상
            for j in range(N-2, -1, -1):
                if board[i][j] == 0:
                    continue
                elif board[i][j] == board[i][j+1]:
                    board[i][j+1] = 2*board[i][j+1]
                    board[i][j] = 0
    # print('3', board)

    # 2. 2) 숫자를 당겨서 0으로 대체된 공간을 없애기
    board = move(board, dir)
    # print('4', board)
    if dir > 1:
        board = rotate_270(board)
    return board


def bfs(board):
    deq = deque()
    deq.append(board)
    max_values = []
    cnt = -1

    while deq:
        cnt += 1

        if cnt == 6:
            return max(max_values)

        for _ in range(len(deq)):

            if cnt == 5:
                max_value = -1
                for i in range(N):
                    for j in range(N):
                        max_value = max(max_value, board[i][j])
                max_values.append(max_value)

            board = deq.popleft()
            for i in range(4):
                temp_board = deepcopy(board)
                temp_board = func_2048(temp_board, i)
                deq.append(temp_board)


# 0, 1, 2, 3  : 우 좌 상 하
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(bfs(board))


################################################




#
# def print_(board):
#     for row in board:
#         print(*row)
#     print()
#
# print_(board)
# board = func_2048(board, 3)
# print_(board)
# board = func_2048(board, 3)
# print_(board)
# board = func_2048(board, 1)
# print_(board)
# board = func_2048(board, 2)
# print_(board)
# board = func_2048(board, 2)
# print_(board)
# print()

# board = func_2048(board, 1)
# print_(board)
# board = func_2048(board, 1)
# print_(board)
# board = func_2048(board, 2)

# N = 4
# # 그림 1~3
# board = [[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]
# print_(board)
# board = func_2048(board, 2)
# print_(board)
# board = func_2048(board, 1)
# print_(board)
#
# # 그림 4~7
# board = [[4, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0]]
# print_(board)
# board = func_2048(board, 0)
# print_(board)
# board = func_2048(board, 2)
# print_(board)
# board = func_2048(board, 0)
# print_(board)
#
# # 그림 8~9
# board = [[2, 0, 2, 8], [0, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
# print_(board)
# board = func_2048(board, 1)
# print_(board)
#
# # 그림 10~11
# board = [[2, 4, 16, 8], [8, 4, 0, 0], [16, 8, 2, 0], [2, 8, 2, 0]]
# print_(board)
# board = func_2048(board, 2)
# print_(board)
#
# # 그림 12~13
# board = [[2, 4, 8, 2], [2, 4, 0, 0], [2, 0, 0, 0], [2, 0, 2, 0]]
# print_(board)
# board = func_2048(board, 2)
# print_(board)
#
#
# # 그림 14~15
# board = [[2, 0, 0, 0], [2, 2, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]
# print_(board)
# board = func_2048(board, 2)
# print_(board)



