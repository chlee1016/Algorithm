# 1. 0인 부분만을 찾는다.
# 2. is promising 함수 만듬
# 3. 행, 열, 3*3 박스 내 검사
# 4. 유망한 숫자들 다 집어 넣기
# 5. 다음 0인 부분으로 넘어간다. (재귀함수 호출)
# 6. 해당 부분을 0으로 다시 초기화 (5.의 재귀함수 내부에서 정답이 없을 경우를 고려)
# 7. 마지막 0까지 모두 넣어봤다면, 출력한다.
# Flag를 별도로 두고 구현해봄
# *arg를 사용해봄
#

board = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
flag = False  # 답 출력 여부를 알리는 flag


def isPromising(i, j):
    promising = [a for a in range(1, 10)]

    # 행열 검사
    for k in range(9):
        # 이렇게 제거해 나가면 결국 blank의 정답 값이 남음
        if board[i][k] in promising:
            promising.remove(board[i][k])
        if board[k][j] in promising:
            promising.remove(board[k][j])

    # 3*3 박스 검사
    # 단순히 3*3 박스가 아니고, 정해진 3*3 박스를 검사하여야 한다.
    # 이렇게 하면 i가 0일때, 1일때, 2일때 탐색 출발점이 같음 (3개씩 묶여짐)
    i = i//3
    j = j//3

    # 다시 좌표로 바꾸어줘야 하니 *3을 함
    for a in range(i*3, i*3+3):
        for b in range(j*3, j*3+3):
            if board[a][b] in promising:
                promising.remove(board[a][b])
    return promising


def sudoku(x):
    # x는 현재 찾고 있는 blank의 index를 의미함.
    # [(0,0), (1,4), (1,7)] 으로 blank가 3개이면 차례로 x = 0, 1, 2 ..
    
    global flag

    if flag:  # 이미 답이 출력 된 경우
        return

    if x == len(blank):  # 모든 blank의 값을 찾았을 경우
        for row in board:
            # 이 부분, *arg를 이용하여 인자를 전달하는 방법
            print(*row)
        flag = True  # 답 출력 여부를 알림
        return

    else:
        i, j = blank[x]
        promising = isPromising(i, j)
        for num in promising:
            board[i][j] = num
            sudoku(x + 1)
            board[i][j] = 0  # 초기화 (정답이 없을 경우를 대비)


sudoku(x=0)

