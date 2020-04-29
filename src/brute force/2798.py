import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
max_update = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_cards = lst[i] + lst[j] + lst[k]
            if sum_cards <= M and sum_cards > max_update:
                max_update = sum_cards
print(max_update)