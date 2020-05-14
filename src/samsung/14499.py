n, m, y, x, k = map(int, input().split())
# x y : 주사위를 놓은 곳의 좌표
# k : 명령의 개수
board = [list(map(int, input().split())) for _ in range(n)]
# 지도의 0이 시작점
cmds = list(map(int, input().split()))

# 역시나 y-1이 북쪽인게 헷갈렸던 문제
# if -1 < nx < m and -1 < ny < n:의 else문을 작성안해줘서 런타임 에러
from collections import deque
deq = deque()
deq.append([y, x])
deq_ver = deque([0, 0, 0, 0])
deq_hor = deque([0, 0, 0, 0])
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]





def copy(ny, nx):
    # copy(ny, nx) 함수의 역할
    # 이동한 칸에 쓰여있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사된다.
    # 칸에 쓰여 있는 수는 0이 된다.
    if board[ny][nx] == 0:
        board[ny][nx] = deq_hor[0]
    else:
        deq_ver[0] = board[ny][nx]
        deq_hor[0] = board[ny][nx]
        board[ny][nx] = 0


for cmd in cmds:
    # cmd,  1 : 동, 2 : 서, 3: 북, 4: 남
    y, x = deq.popleft()
    # print('y, x', y, x)
    nx = x + dx[cmd-1]
    ny = y + dy[cmd-1]

    if -1 < nx < m and -1 < ny < n:
        # print(ny, nx)
        deq.append([ny, nx])
        if cmd == 1:  # 동쪽으로 이동
            deq_hor.rotate(-1)  # 회전 후
            deq_ver[0] = deq_hor[0]  # 아랫면 매칭
            deq_ver[2] = deq_hor[2]  # 윗면 매칭
            copy(ny, nx)
            print(deq_hor[2])

        elif cmd == 2:  # 서쪽으로 이동
            deq_hor.rotate(1)
            deq_ver[0] = deq_hor[0]
            deq_ver[2] = deq_hor[2]
            copy(ny, nx)
            print(deq_hor[2])

        elif cmd == 3:  # 북쪽으로 이동
            deq_ver.rotate(-1)
            deq_hor[0] = deq_ver[0]
            deq_hor[2] = deq_ver[2]
            copy(ny, nx)
            print(deq_hor[2])

        elif cmd == 4:  # 남쪽으로 이동
            deq_ver.rotate(1)
            deq_hor[0] = deq_ver[0]
            deq_hor[2] = deq_ver[2]
            copy(ny, nx)
            print(deq_hor[2])
    else:  # 나가는 경우 아무것도 출력하지 않고 현재 위치 다시 입력
        deq.append([y, x])



