T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    board = [[0]*n for _ in range(k+1)]

    for j in range(k+1):
        for i in range(n):
            if j == 0:  # 제일 아랫층
                board[j][i] = i+1
            elif i == 0:  # 제일 왼쪽 층
                board[j][i] = 1
            else:  # 왼쪽 꺼 + 아랫 쪽 꺼
                board[j][i] = board[j][i-1] + board[j-1][i]
    print(board[k][n-1])
    # for row in board:
    #     print(*row)
    # print()