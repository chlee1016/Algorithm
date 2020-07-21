N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

a = [list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW')]
b = [list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB')]


def check_board(y, x):
    a_cnt = 0
    b_cnt = 0
    for i in range(8):
        for j in range(8):
            if board[i+y][j+x] != a[i][j]:
                a_cnt += 1
            if board[i+y][j+x] != b[i][j]:
                b_cnt += 1
    return min(a_cnt, b_cnt)



cnts = []
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt = check_board(i, j)
        cnts.append(cnt)

print(min(cnts))


