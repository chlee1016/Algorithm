from itertools import combinations
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

diff = 300000
sum_cards = 0
for nums in combinations(numbers, 3):
    if M - sum(nums) >= 0:  # M을 넘지 않으면서
        if diff > M - sum(nums):
            diff = M - sum(nums)
            sum_cards = sum(nums)
    else:
        continue
print(sum_cards)