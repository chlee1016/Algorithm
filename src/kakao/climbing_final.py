#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.

# 1st try : simple case
# def climbingLeaderboard(scores, alice):
#     scores = list(set(scores))
#     scores.sort(reverse=True)
#     output = []
#     for i in range(len(alice)):
#         alice_score = alice[i]
#         rank = 1
#         for score in scores:
#             # 크기 비교
#             if score > alice_score:
#                 rank += 1
#         output.append(rank)
#     return output

# 2nd try : to reduce the computation time
def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse=True)
    # print(len(scores)) # 5
    half_idx = int(len(scores) / 2) # 2
    quat_idx = int(len(scores) / 4)
    # print(half_idx)
    output = []
    for i in range(len(alice)):
        alice_score = alice[i]
        # 아래 3/4쪽이면
        if scores[3 * quat_idx] > alice_score:
            # 인덱스는 3/4부터 시작하고
            rank = 3 * quat_idx + 1
            # 3/4쪽부터 크기 비교 시작
            for score in scores[(3 * quat_idx):]:
                # 크기 비교
                if score > alice_score:
                    rank += 1
            output.append(rank)


        elif scores[half_idx] > alice_score:
            # 인덱스는 반쪽부터 시작하고
            rank = half_idx + 1
            # 반쪽부터 크기 비교 시작
            for score in scores[half_idx:]:
                # 크기 비교
                if score > alice_score:
                    rank += 1
            output.append(rank)

        elif scores[quat_idx] > alice_score:
            # 인덱스는 1/4쪽부터 시작하고
            rank = quat_idx + 1
            # 1/4쪽부터 크기 비교 시작
            for score in scores[quat_idx:]:
                # 크기 비교
                if score > alice_score:
                    rank += 1
            output.append(rank)

        else:
            rank = 1
            for score in scores:
                # 크기 비교
                if score > alice_score:
                    rank += 1
            output.append(rank)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    # scores_count = 7
    # scores = [100, 100, 50, 40, 40, 20, 10]
    # alice_count = 4
    # alice = [5, 25, 50, 120]
    # result = climbingLeaderboard(scores, alice)
    # print(result)
    # expected output: 6 4 2 1

