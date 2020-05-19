# 벽 또는 자기자신의 몸과 부딪히면인데, 자기자신과 부딪히는 경우를 생각하지 않았다.
# 방향 변환 정보는 X초가 끝난 뒤에 이동인데, X초가 시작될 때 변환시켰다.
# 문제를 잘못 읽어서 dir_inf_dic[count] == 'L':를 dir_inf_dic[count] == 'C':로 잘못 썼다.
# list.index() 함수를 잘 이용하였다.
# rotate 함수를 문제의도에 맞게 잘 이용하였다.

n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    apple_y, apple_x = list(map(int,input().split()))
    board[apple_y-1][apple_x-1] = 2

dir_inf_dic = {}
l = int(input())
for _ in range(l):
    key, value = list(input().split())
    dir_inf_dic[int(key)+1] = value


# print(board)
# print(dir_inf_dic)
######################

count = 0
from collections import deque
direction = deque([1, 0, 0, 0])
#  deque([0,0])이 아니다!
snake = deque([[0, 0]])  # 뱀이 존재하는 위치 정보 저장
dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]

while True:
    y, x = snake[-1]  # 머리 정보 불러오기
    count += 1
    # 방향 바꾸기
    if count in dir_inf_dic:
        if dir_inf_dic[count] == 'D':  # D일 때 오른쪽, C일 때 왼쪽 회전
            direction.rotate(1)
        elif dir_inf_dic[count] == 'L':
            direction.rotate(-1)
    idx = direction.index(1)

    # board[y][x] = 1
    # for row in board:
    #     print(*row)
    # print()
    #  머리 이동
    nx = x + dx[idx]
    ny = y + dy[idx]

    if -1 < nx < n and -1 < ny < n and [ny, nx] not in snake:  # 0~ n-1의 보드 안에 있으면 이동
        snake.append([ny, nx])  # 몸 길이를 늘려 머리를 다음칸에 위치시킴
        if board[ny][nx] == 2:  # 만약 사과가 존재하면
            board[ny][nx] = 0  # 사과는 없어짐
            # 꼬리는 움직이지 않는다.

        elif board[ny][nx] == 0:  # 만약 사과가 없으면
            snake.popleft()  # 몸 길이를 줄여서 꼬리가 위치한 칸을 비워줌

    else:  # 만약 벽을 만나면 종료하고 게임이 끝나는 시간 출력
        print(count)
        break

# from collections import deque
# a = deque([[1,0],[2,1], [4,5]])
# print([2,1] in a)