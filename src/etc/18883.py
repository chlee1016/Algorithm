n, m = map(int, input().split())
# 시간 2배 줄일 수 있는 코드
for i in range(n):
    a = list(range(1 + i*m, (i+1)*m+1))
    print(*a)

# for i in range(n):
#     for j in range(m):
#         if (j+1) % m == 0:
#             print(j + 1 + i * m, end='')
#         else:
#             print(j + 1 + i * m, end=' ')
#     print()

