board = [list(map(int, input().split())) for _ in range(9)]
lst = [[i, j] for i in range(9) for j in range(9) if board[i][j] == 0]
lst.reverse()  # pop(0) 대신 pop()을 사용하기 위함, 필수는 아님
N = len(lst)
flag = False

def check_board(y, x, val):
    for i in range(3):
        for j in range(3):
            if board[y//3*3+i][x//3*3+j] == val:
                return False

    for i in range(9):  # 가로 검사
        if board[y][i] == val:
            return False

    for j in range(9):  # 세로 검사
        if board[j][x] == val:
            return False

    return True


def solve(depth):
    global flag

    if flag:  # 이미 답이 출력 된 경우,
        # 여러 개의 답이 출력되는 것을 방지하기 위해서 flag를 둠
        # 이걸 안해서 틀렸었음
        return

    if depth == N:
        for row in board:
            print(*row)
        flag = True
        return

    for val in range(1, 10):
        y, x = lst[-1]
        if check_board(y, x, val):
            lst.pop()
            board[y][x] = val

            solve(depth+1)

            lst.append([y, x])
            board[y][x] = 0


solve(0)
