from collections import deque

def get_score(status):
    score = 0
    for i in range(4):
        if status[i][0] == 1:
            score += (2**i)
    return score


def get_directions(idx, direction):
    directions = [0, 0, 0, 0]
    directions[idx] = direction
    visit = [0, 0, 0, 0]
    deq = deque()
    deq.append(idx)

    if idx == 0:
        if status[idx][right] != status[idx + 1][left]:
            directions[idx + 1] = -directions[idx]
        if status[idx + 1][right] != status[idx + 2][left]:
            directions[idx + 2] = -directions[idx + 1]
        if status[idx + 2][right] != status[idx + 3][left]:
            directions[idx + 3] = -directions[idx + 2]

    elif idx == 1:
        # 오른쪽 전파
        if status[idx][right] != status[idx + 1][left]:
            directions[idx + 1] = -directions[idx]
        if status[idx + 1][right] != status[idx + 2][left]:
            directions[idx + 2] = -directions[idx + 1]

        # 왼쪽 전파
        if status[idx][left] != status[idx - 1][right]:
            directions[idx - 1] = -directions[idx]

    elif idx == 2:
        # 오른쪽 전파
        if status[idx][right] != status[idx + 1][left]:
            directions[idx + 1] = -directions[idx]
        # 왼쪽 전파
        if status[idx][left] != status[idx - 1][right]:
            directions[idx - 1] = -directions[idx]
        if status[idx - 1][left] != status[idx - 2][right]:
            directions[idx - 2] = -directions[idx - 1]

    elif idx == 3:
        # 왼쪽 전파
        if status[idx][left] != status[idx - 1][right]:
            directions[idx - 1] = -directions[idx]
        if status[idx - 1][left] != status[idx - 2][right]:
            directions[idx - 2] = -directions[idx - 1]
        if status[idx - 2][left] != status[idx - 3][right]:
            directions[idx - 3] = -directions[idx - 2]

    return directions


if __name__ == '__main__':
    status = [deque(map(int, list(input()))) for _ in range(4)]  # N pole : 0, S pole : 1
    # status = [deque(map(int, list('10101111'))), deque(map(int, list('01111101'))),\
    # deque(map(int, list('11001110'))), deque(map(int, list('00000010')))]
    k = int(input())
    move = [list(map(int, input().split())) for _ in range(k)]
    left = 6
    right = 2
    # 1 : clockwise
    # -1 : counter clockwise

    for num, direction in move:
        idx = num - 1
        directions = get_directions(idx, direction)
        for i in range(4):
            status[i].rotate(directions[i])

    score = get_score(status)
    print(score)

