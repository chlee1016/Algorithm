n, m = list(map(int, input().split()))

out = []
# visit = [False] * n
def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        # visit[i] = True
        out.append(i+1)
        solve(depth+1, n, m)
        # visit[i] = False
        out.pop()


solve(0, n, m)


