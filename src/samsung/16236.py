# https://dailyheumsi.tistory.com/59
# 도달할 수 있는지 없는지는 BFS를 하다보면 자연스레 알게 됨.
# 도달할 수 없으면 해당 좌표로 BFS가 가지 못함
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

from collections import deque


# def is_edible(board, shark_s):
#     # 하나라도 잡아먹을 수 있으면 True,
#     # 아니면 False를 리턴하는 함수
#
#     for y in range(n):
#         for x in range(n):
#             # if board[y][x] == 9:
#             #     continue
#             if board[y][x] < shark_s and board[y][x] != 0:
#                 return True
#             # 여기서 else문으로 return을 주는게 아니라
#             # 아래에서 default로 return을 주어야 한다.
#     return False


def bfs():
    deq = deque()
    shark_s = 2
    sec = 0
    answer = 0
    cnt = 0
    flag = False
    for y in range(n):  # 처음 상어의 위치 추가
        for x in range(n):
            if board[y][x] == 9:
                deq.append([y, x])
                board[y][x] = 0


    # 먹을 수 있는 물고기가 존재하면 탐색 시작
    while len(deq) != 0:
        sec += 1
        deq = deque(sorted(deq))  # sort는 기본 오름차순이다.
        # print('sorted', deq)
        # 어차피 거리는 같을 것이기에
        # 가장 위에 있고, 왼쪽에 있는 물고기 먼저 탐색
        for _ in range(len(deq)):  # 여기서 먹을 수 있는 물고기 후보가 담겨져 있다.
            y, x = deq.popleft()
            visit[y][x] = 1

            if board[y][x] != 0 and board[y][x] < shark_s:
                sec -= 1  # 시간 추가 -> 물고기 먹기 -> 시간 제거
                # 단지 물고기를 먹는 액션은 시간추가하면 안되므로
                board[y][x] = 0
                cnt += 1
                if cnt == shark_s:  # 상어의 크기 증가
                    shark_s += 1
                    cnt = 0

                # for row in board:
                #     print(*row)
                # print('size of shark', shark_s)
                # print('seconds', sec)

                deq = deque()
                deq.append([y, x])  # 상어의 다음위치 지정
                for i in range(n):
                    for j in range(n):
                        if i == y and j == x:
                            visit[i][j] = 1
                        else:
                            visit[i][j] = 0
                # flag = True
                answer = sec
                # 먹었을 때의 시간을 저장해둔다.
                # 덮어쓰고 덮어쓰고 하다가, ans에는 최종 시간이 저장된다.
                break

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if -1 < nx < n and -1 < ny < n and visit[ny][nx] == 0:
                    if board[ny][nx] <= shark_s or board[ny][nx] == 0:
                        # 상어가 지나가는 부분
                        deq.append([ny, nx])
                        visit[ny][nx] = 1
                    # append하고 그것을 바로 먹으러 가는 것이 아니라
                    # 모두 append하고 정렬하고 pop 후 먹기
                    # elif board[ny][nx] < shark_s:  # 잡아 먹을 수 있는 물고기 체크






            #
            # if check == 1:
            #     # 먹을 수 있는 물고기가 1마리라면,
            #     sy, sx = edible[0] # 출발점 재설정
            #     deq = deque()
            #     deq.append([sy, sx])
            #
            #     # 그 물고기를 먹으러 간다.
            #     # 먹은 곳은 빈칸으로 만들기
            #     board[sy][sx] = 0
            #     cnt += 1
            #     if cnt == shark_s:  # 상어의 크기 증가
            #         shark_s += 1
            #         cnt = 0
            #     # print(sec)
            #
            # elif check > 1:
            #     # 이 부분만 수정되면 됨
            #     # input : edible - 먹을 수 있는 물고기 리스트
            #     # output : sy, sx - 최종적으로 먹을 물고기 위치
            #     # 결국 sy, sx를 찾으면 됨
            #     # 먹을 수 있는 물고기가 1마리보다 많다면,
            #     # 가장 가까운 물고기 선택
            #     dist = []
            #     for y, x in edible:
            #         dist.append(abs(y-sy) + abs(x-sx))
            #     sy, sx = dist.index(max(dist))
            #     deq = deque()
            #     deq.append([sy, sx])
            #
            #     # 그 물고기를 먹으러 간다.
            #     board[sy][sx] = 0
            #     cnt += 1
            #     if cnt == shark_s:  # 상어의 크기 증가
            #         shark_s += 1
            #         cnt = 0



    print(answer)
    return


bfs()