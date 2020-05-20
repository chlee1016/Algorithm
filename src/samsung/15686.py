n, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

from itertools import combinations
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            houses.append((y, x))
        elif board[y][x] == 2:
            chickens.append((y, x))

# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
# 도시의 치킨 거리의 최솟값을 출력한다.
min_city_chi_dist = 1000000
for chicken_set in combinations(chickens, m):
    city_chi_dist = 0
    for house in houses:
        chi_dist = 1000000
        for chicken in chicken_set:
            dist = abs(house[0]-chicken[0])+abs(house[1]-chicken[1])
            chi_dist = min(dist, chi_dist)
        city_chi_dist += chi_dist
    min_city_chi_dist = min(min_city_chi_dist, city_chi_dist)
print(min_city_chi_dist)
























# import sys
# sys.setrecursionlimit(10000)
#
# from collections import deque
# chicken_list = deque()
# def chicken(depth):
#     if depth == m:
#         bfs()
#         return
#     else:
#         for y in range(n):
#             for x in range(n):
#                 if board[y][x] == 2:  # 치킨 집이면
#                     chicken_list.append([y, x])  # 치킨 집 목록에 추가하고
#                     chicken(depth+1)  # 그 다음 치킨집 추가
#                     chicken_list.popleft()  # 수평적 중복 제거
#
#
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# min_count = 10000
#
# import copy
#
#
# def bfs():
#     # m개의 치킨 집 목록과 집이 주어져 있을 때,
#     # 각 치킨집과 가정 먼저 도달하는 집을 구하고
#     # 거리를 구해서
#     # 그 합을 계산하면 도시의 치킨 거리가 됨
#     global min_count
#     dist = 0
#     temp_chk_list = copy.deepcopy(chicken_list)
#     temp_board = copy.deepcopy(board)
#     while len(temp_chk_list) != 0:
#         dist += 1
#         for _ in range(len(temp_chk_list)):
#             y, x = temp_chk_list.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#
#                 if -1 < nx < n and -1 < ny < n:
#                     temp_chk_list.append([ny, nx])
#                     if temp_board[ny][nx] == 1:  # 집이면
#                         temp_board[ny][nx] = dist
#
#     for ry, rx in chicken_list:
#         min_count = min(temp_board[ry][rx], min_count)
#     print(min_count)
#
#
#
# chicken(0)




