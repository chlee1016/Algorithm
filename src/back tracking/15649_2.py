N, M = map(int, input().split())
output = [0]*M


def solve(depth):
    if depth == M:
        print(' '.join(map(str, output)))
        return
    for i in range(N):
        if i+1 not in output:
            output[depth] = i+1
            solve(depth+1)
            output[depth] = 0


solve(0)