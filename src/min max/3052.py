lst = [int(input()) % 42 for _ in range(10)]
exist = [0] * 42

for j in range(42):
    for i in lst:
        if i == j:
            exist[j] = 1

print(sum(exist))
