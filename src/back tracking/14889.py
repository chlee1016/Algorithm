n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# members = set([i for i in range(n)])
members = set(range(n))

from itertools import combinations
teams = combinations(members, n//2)
start_score = []
link_score = []
for team in teams:
    start_team = set(team)
    link_team = members - start_team

    score = 0
    for start_xy in combinations(start_team, 2):
        a, b = start_xy
        score += matrix[a][b] + matrix[b][a]
    start_score.append(score)

    score = 0
    for link_xy in combinations(link_team, 2):
        c, d = link_xy
        score += matrix[c][d] + matrix[d][c]
    link_score.append(score)

diff = []

for i in range(len(start_score)):
    diff.append(abs(start_score[i] - link_score[i]))
print(min(diff))

