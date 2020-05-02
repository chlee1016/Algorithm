n = int(input())
scores = list(map(int, list(input().split())))
m = max(scores)
avg = (sum(scores) / m * 100) / n
print(avg)
