n, m = list(map(int, input().split()))

out = []


def solve(depth, idx, n, m):
    if m == depth:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, n):
        out.append(i+1)
        solve(depth+1, i, n, m)
        out.pop()


solve(0, 0, n, m)
