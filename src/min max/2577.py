number = [int(input()) for _ in range(3)]
mul = number[0] * number[1] * number[2]
lst = list(map(int, list(str(mul))))
cnt = [0] * 10
for j in range(10):
    for i in lst:
        if i == j:
            cnt[j] += 1
    print(cnt[j])

