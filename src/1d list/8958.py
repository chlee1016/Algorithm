T = int(input())
for _ in range(T):
    result = list(input())
    scores = [0] * len(result)
    cnt = 0
    for i in range(len(result)):
        if result[i] == 'O':
            cnt += 1
            scores[i] = cnt

        else:
            scores[i] = 0
            cnt = 0

    print(sum(scores))

