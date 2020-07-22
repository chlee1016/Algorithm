# from itertools import combinations
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

start_team = []
result = 1000000000
members = set(range(N))


def calc_score(start_team):
    global result
    link_team = members - start_team

    start_score = 0
    link_score = 0

    for a in start_team:
        for b in start_team:
            start_score += S[a][b]

    for c in link_team:
        for d in link_team:
            link_score += S[c][d]

    # for a, b in combinations(start_team, 2):
    #     start_score += S[a][b] + S[b][a]
    #
    # for c, d in combinations(link_team, 2):
    #     link_score += S[c][d] + S[d][c]

    result = min(result, abs(start_score - link_score))


def solve(depth, start_idx):
    if depth == N//2:
        calc_score(set(start_team))
        return

    for i in range(start_idx, N):
        if i not in start_team:
            start_team.append(i)
            solve(depth+1, i+1)
            start_team.pop()

solve(0,0)

print(result)