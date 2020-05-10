#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'maximumProfit' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY price as parameter.


def maximumProfit(price):
    # Write your code here
    # n = 6
    # price = [3, 4, 5, 3, 5, 2]
    # n = 3
    # price = [5, 3, 2]
    # 살 때, 각 시간당 하나만 살 수 있음
    # 팔 때, 다 팔 수 있음
    # 아무것도 안할 수도 있다.
    max_price = 0
    profit = 0
    n = len(price)
    # 각 시간 만큼 반복
    for i in range(n - 1, -1, -1):
        # 뒤에서 부터 검사해서 max_price 찾기
        # 만약 현재 price가 maximum이면
        if price[i] > max_price:
            # max_price를 업데이트
            max_price = price[i]

        # 현재 price가 maximum이 아니면
        else:
            # profit 업데이트
            profit = profit + max_price - price[i]

    return profit


if __name__ == '__main__':
    n = 6
    price = [3, 4, 5, 3, 5, 2]
    max_profit = maximumProfit(price)
    print(max_profit)
