n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [[(0,0), (0,1), (1,0), (1,1)],
       [(0,0), (0,1), (0,2), (0,3)],
       [(0,0), (1,0), (2,0), (3,0)],
       [(0,0), (1,0), (2,0), (2,1)],
       [(0,0), (1,0), (0,1), (0,2)],
       [(0,0), (0,1), (1,1), (2,1)],
       [(1,0), (1,1), (1,2), (0,2)],
       [(0,0), (1,0), (1,1), (1,2)],
       [(0,0), (0,1), (0,2), (1,2)],
       [(2,0), (0,1), (1,1), (2,1)],
       [(0,0), (1,0), (2,0), (0,1)],
       [(0,0), (1,0), (1,1), (2,1)],
       [(0,0), (1,0), (2,0), (1,1)],
       [(0,0), (0,1), (1,1), (1,2)],
       [(0,0), (0,1), (0,2), (1,1)],
       [(1,0), (1,1), (0,1), (0,2)],
       [(1,0), (2,0), (0,1), (1,1)],
       [(1,0), (1,1), (1,2), (0,1)],
       [(1,0), (0,1), (1,1), (2,1)]
       ]




# max_sum = -1
#
# for y in range(n):
#     for x in range(m):
#         for i in range(19):
#             tet_sum = 0
#             for j in range(4):  # 하나의 테트리미노에 대해서 합 계산
#                 ny = y + dxy[i][j][0]
#                 nx = x + dxy[i][j][1]
#
#                 if -1 < nx < m and -1 < ny < n:
#                     tet_sum += board[ny][nx]
#                 else:
#                     break
#             else:  # break문을 만나지 않으면
#                 if tet_sum > max_sum:
#                     max_sum = tet_sum  # 최댓값 갱신
#
#
# print(max_sum)


max_sum = -1
for k in dxy:
    for y in range(n):
        for x in range(m):
                tet_sum = 0
                for j in range(4):  # 하나의 테트리미노에 대해서 합 계산
                    ny = y + k[j][0]
                    nx = x + k[j][1]
                    if -1 < nx < m and -1 < ny < n:
                        tet_sum += board[ny][nx]
                    else:
                        break
                else:  # break문을 만나지 않으면
                    if tet_sum > max_sum:
                        max_sum = tet_sum  # 최댓값 갱신


print(max_sum)