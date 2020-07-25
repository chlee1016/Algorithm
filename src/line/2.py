# N = int(input())
# tops = list(map(int, input().split()))
# result = [0]*N
#
#
# for i in range(N):
#     if i != 0:
#         for j in range(i-1, -1, -1):
#             if tops[j] > tops[i]:
#                 result[i] = j+1
#                 break
#
# print(*result)


N = int(input())
tops = list(map(int, input().split()))  # height, not idx
result = [0]*N  # idx
stack = []  # idx

for i in range(N):
    while stack and tops[stack[-1]] < tops[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)