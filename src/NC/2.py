# Solution 1
prices = [5, 3, 7, 9, 5, 2, 4, 9, 10, 6]
answer = []

for i in range(len(prices)):
    cnt = 0
    for j in range(i + 1, len(prices)):
        if prices[i] < prices[j]:
            cnt += 1
    answer.append(cnt)
# expected result : [5, 7, 3, 1, 3, 4, 3, 1, 0, 0]


# Solution 2 (submitted)
prices = [5, 3, 7, 9, 5, 2, 4, 9, 10, 6]
answer = []

sorted_prices = sorted(prices)  # 가격 순서대로 정렬된 배열

for i in range(len(prices)):  # 요소 하나씩을 꺼내 와서
    # print('prices', prices)
    # print('sorted_prices', sorted_prices)
    # print('prices[i]', prices[i])
    idx = sorted_prices.index(prices[i])  # 몇 번째 인덱스인지 구하기
    num = sorted_prices[idx]  # 현재 숫자 저장
    # print('idx before', idx)
    max_num = sorted_prices[-1]  # 최대 숫자 저장
    if num == max_num:
        cnt = 0
        answer.append(cnt)
        sorted_prices.pop()

    else:
        for j in range(idx, len(sorted_prices) - 1):
            if num == sorted_prices[j + 1]:
                idx += 1
                continue
            else:
                idx += 1
                break
        # print('idx after', idx)
        # print('len(sorted_prices)', len(sorted_prices))
        cnt = len(sorted_prices) - idx
        # print('result:', cnt)
        answer.append(cnt)
        del sorted_prices[idx - 1]
    # print()
print(answer)
# expected result : [5, 7, 3, 1, 3, 4, 3, 1, 0, 0]