n, m = map(int, input().split())
visit = [False] * n
out = []
out_all = []

# 1. 순열을 담은 list를 오름차순으로 정리한 후(sorted()), 문자열로 만든다.
# 2. 출력용 list에 그 문자열이 없다면, append한다.
# 3. 출력용 list를 한 줄씩 출력한다.

# solution 1
# def solve(depth, n, m):
#     if depth == m:
#         out_str = ' '.join(map(str, sorted(out)))
#         if out_str not in out_all:
#             out_all.append(out_str)
#         # print(' '.join(map(str, out)))
#         return
#
#     for i in range(n):
#         if not visit[i]:
#             visit[i] = True
#             out.append(i+1)
#             solve(depth+1, n, m)
#             visit[i] = False
#             out.pop()
# solve(0, n, m)

# for i in out_all:
#     print(i)


# solution 2
# 바로 이전의 idx 값을 넘겨주어, idx 이하는 탐색하지 않도록 만듬
def solve(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, n):
        visit[i] = True
        out.append(i+1)
        solve(depth+1, i+1, n, m)
        visit[i] = False
        out.pop()


solve(0, 0, n, m)


