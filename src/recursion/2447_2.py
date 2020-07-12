# 이 벽을 넘지 못하면 발전은 없다.
N = int(input())

board = [[' '] * N for _ in range(N)]


def star(y, x, N):
    if N == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    board[y+i][x+j] = ' '
                else:
                    board[y+i][x+j] = '*'
    else:
        for a in range(3):
            for b in range(3):
                if a == 1 and b == 1:
                    continue
                else:
                    star(y + (N // 3) * a, x + (N // 3) * b, N // 3)


star(0, 0, N)

# 출력
for row in board:
    for char in row:
        print(char, end='')
    print()


# 재귀 호출 할 때, star(y + (N // 3) * a, x + (N // 3) * b, N // 3) 대신에
# star((N // 3) * a, (N // 3) * b, N // 3)를 해서 원하는 출력이 생성되지 않았다.
# 재귀함수 구현할 때, 종료 조건을 생각하고
# 재귀로 입력되는 값에 어떤 것이 들어가는지,
# 그 입력 값에는 어떠한 규칙이 있는지를 찾는다.
# 재귀함수가 호출되는 형태를 트리 형태로 구현해보면서,
# 입력 값이 들어 갔을 때 올바르게 동작하는지를 확인한다.

