N = int(input())
# print(int(N % 10))
# print(int(N % 100 / 10))  # 십의자리
# print(int(N % 1000 / 100))  # 백의자리
# print(int(N % 10000 / 1000))
# print(int(N % 100000 / 10000))
# print(int(N % 1000000 / 100000))  # 십만의 자리
# print(int(N % 10000000 / 1000000))  # 백만의 자리

generator = []
for x in range(N):
    candidate = x + int(x % 10000000 / 1000000) + int(x % 1000000 / 100000) \
        + int(x % 100000 / 10000) + int(x % 10000 / 1000) \
        + int(x % 1000 / 100) + int(x % 100 / 10) \
        + int(x % 10)
    if N == candidate:
        generator.append(x)

if len(generator) == 0:
    print(0)
else:
    print(min(generator))


