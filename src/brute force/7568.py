# 덩치 순위 계산

# example input
# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155
# 동차 랭킹에 대해서 따로 처리를 해주어야하는 줄 알았는데,
# n 명을 n-1번씩 비교하니까 편하게 자동으로 처리가 되었다.


def dungchi():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    rank = [1 for _ in range(n)]

    for i in range(len(data)):
        # 비교 하고자 하는 index
        for j in range(len(data)):
            # 비교 대상 index
            if i == j:
                continue
            else:
                if data[i][0] < data[j][0] and \
                        data[i][1] < data[j][1]:
                    rank[i] += 1
    for i in range(len(rank)):
        print(rank[i], end=' ')


dungchi()
