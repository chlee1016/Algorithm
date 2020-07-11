# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라.
# 단, 이동 횟수는 최소가 되어야 한다.
# 아래 그림은 원판이 5개인 경우의 예시이다.

# n개의 원판 디스크를 옮길 때, 먼저 n-1개의 원판을 중간에 놓고,
# 제일 큰 원판을 3으로 옮긴다. 이후 다시 n-1개의 원판을 2에서 3으로 옮긴다.


def hanoi(n, start, mid, end):
    if n == 1:
        # print(start, end)
        move.append([start, end])

    elif n >= 2:
        hanoi(n - 1, start, end, mid)  # n-1개의 원반들을 목적지가 아닌 mid로 이동
        # print(start, end)  # 제일 아래 원반을 end로 이동
        move.append([start, end])
        hanoi(n - 1, mid, start, end)  # n-1개의 원반들을 제일 아래 원반의 위로 이동


n = int(input())
move = []
hanoi(n, 1, 2, 3)
print(len(move))
for i in range(len(move)):
    print(move[i][0], end=' ')
    print(move[i][1])
