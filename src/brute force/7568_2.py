N = int(input())
lst = []
ranks = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])

for x, y in lst:
    rank = 1
    for p, q in lst:
        if x < p and y < q:  # 비교 대상에 더 큰 덩치가 있으면
            rank += 1  # 순위 밀려남
    ranks.append(rank)
print(*ranks)