from collections import deque
N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         # board[i].rotate(1)
#
def rotate(row, n):
    return row[-n:] + row[:-n]


a = [1, 2, 3]
b = [4, 5, 6]

#
# dir = 3
# cnt_zero = 2
# print(rotate(a+b, ((-1)**(dir%2))*cnt_zero))
#
board = [[2, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# 2. 2) 숫자를 당겨서 0으로 대체된 공간을 없애기
cnt_zero = 0

for i in range(N):
    for j in range(N - 1, -1, -1):
        if board[i][j] == 0:
            cnt_zero += 1
        else:
            if cnt_zero != 0:

                # pop(idx(zero))
                board[i] = rotate(board[i], ((-1) ** (dir % 2)) * cnt_zero)
                print(board[i])
                cnt_zero = 0