# 첫 줄에 테스트케이스의 개수 T가 주어진다.
# T는 최대 1,000,000이다.
# 다음 T줄에는 각각 두 정수 A와 B가 주어진다.
# A와 B는 1 이상, 1,000 이하이다.

from sys import stdin

T = int(input())
for i in range(T):
    A, B = map(int, stdin.readline().rstrip().split())
    print(A+B)
