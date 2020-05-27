# n, m, h = map(int, input().split())
# board = [[0]*n for _ in range(h)]
#
# # 현재의 사다리 상태를 저장하는 함수
# for _ in range(m):
#     y, x = map(int, input().split())
#     board[y-1][x-1] = 1  # 사다리가 있는 왼쪽 칸에 1로 표시
#
#
# def ladder():  # 사다리 게임을 해서, 원하는 결과 값인지를 출력하는 함수
#     for x in range(n):
#         k = x  # k는 사다리 게임 중 현재 x 위치를 나타냄
#         # 각 열마다 테스트
#         for y in range(h):
#             if board[y][k] == 1:  # 현재 칸에 사다리가 있으면
#                 k += 1  # 우측 칸 검사
#             elif 0 < k and board[y][k-1] == 1:
#                 # 이때 범위를 벗어나지 않고, 좌측에 사다리가 있으면
#                 # 좌측으로 이동
#                 k -= 1
#         if k != x:  # h까지 내려왔을 때 k와 x가 다르다는 건, 문제가 요구하는 조건 충족 x
#             return False
#     return True  # 함수 default 값 지정
#
#
# ans = 4
#
# def solve(cnt, y, x):
#     # cnt는 현재 테스트 하는 사다리의 갯수
#     global ans
#     if cnt >= ans:  # 종료 조건, 답이 나와 있는데 재귀를 더 하는 경우
#         return
#     if ladder():  # 1개일때도, 2개일때도, 3개일때도 True 가능, 그래서 ans = cnt로 쓰면 안됨
#         ans = min(ans, cnt)
#         return
#     if cnt == 3:  # ladder 검사를 하고 났는데 return이 아니고 cnt가 3이다 -> print(-1)
#         return
#
#
#     for i in range(y, h):
#         if i == y:
#             k = x
#         else:
#             k = 0
#         for j in range(k, n-1):
#             if board[i][j] == 1:
#                 continue
#             else:
#                 board[i][j] = 1  # 사다리 놓기
#                 solve(cnt+1, i, j+2)  # 사다리를 일렬로 놓지 않게 두칸 띄워서 탐색
#                 board[i][j] = 0  # 수평적 간섭제거
#
#
# solve(0, 0, 0)
# if ans >= 4:
#     print(-1)
# else:
#     print(ans)




n, m, h = map(int, input().split())
board = [[0]*n for _ in range(h)]
for _ in range(m):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1




def ladder(): # 사다리타기 게임을 해서 정답이 나오는지 여부를 리턴하는 함수
    for x in range(n):
        k = x
        for y in range(h):
            if board[y][k] == 1:
                k += 1
            elif k > 0 and board[y][k-1] == 1:
                k -= 1
        if k != x:
            return False
    return True


ans = 4
def solve(cnt, y, x):
    global ans
    if cnt >= ans:
        return
    if ladder():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return

    for i in range(y, h):
        if i == y:
            k = x
        else:
            k = 0
        for j in range(k, n-1):
            if board[i][j] == 1:  # 사다리가 있으면 통과
                continue

            else:
                board[i][j] = 1
                solve(cnt+1, i, j+2)
                board[i][j] = 0



solve(0, 0, 0)
if ans >= 4:
    print(-1)
else:
    print(ans)

