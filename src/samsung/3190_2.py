from collections import deque
N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 'A'  # 사과의 위치 표시




# lst[cnt] -> return index
# lst.index(cnt)

L = int(input())
dir_info = {}
for _ in range(L):
    cnt, direction = input().split()
    dir_info[int(cnt)] = direction

# dir_info[3] = 'D'
# dir_info[15] = 'L'
# dir_info[1] -> error 생겨
# 키가 있는 것은 value 리턴
# 키가 없으면 None 리턴
# dir_info.get(1) -> return None
# dir_info.get(3) -> return 'D'


def change_dir(dir_info, i):
    ni = None
    if dir_info == 'L':  # 왼쪽으로 회전
        if i == 0:
            ni = 3
        else:
            ni = i - 1
    elif dir_info == 'D':  # 오른쪽으로 회전
        if i == 3:
            ni = 0
        else:
            ni = i + 1
    return ni


cnt = 0
board[0][0] = 1  #초기 위치 설정
deq = deque()
deq.append([0, 0, 1])  # y, x, direction

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# dy[0] dx[0] 북쪽
# 북 -> 동 -> 남 -> 서

while True:
    # print(cnt)
    # for row in board:
    #     print(*row)
    # print()
    y, x, i = deq[-1]  # 머리 정보 가져오기

    if dir_info.get(cnt) is not None:  # 방향을 바꾸어야 할 때면
        i = change_dir(dir_info[cnt], i)  # 방향 전환

    # 0초부터 시작. 방향 바꾸는 것부터 체크하고 이동 시작
    cnt += 1
    ny = y + dy[i]
    nx = x + dx[i]

    if -1 < ny < N and -1 < nx < N:
        if board[ny][nx] == 1:
            print(cnt)
            break

        deq.append([ny, nx, i])
        if board[ny][nx] == 'A':  # 사과가 있으면
            board[ny][nx] = 1

        else:  # 사과가 없으면
            board[ny][nx] = 1
            tail_y, tail_x, _ = deq.popleft()
            board[tail_y][tail_x] = 0

    else:
        print(cnt)
        break

