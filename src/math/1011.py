T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    gap = y-x
    i = 1

    while True:
        if gap > 2*i:
            gap -= 2*i
            i += 1
        else:
            if gap <= i:
                output = 2*i-1
            else:
                output = 2*i
            print(output)
            break


# 이동 횟수의 최솟값을 구하는 게 목적
# x와 y 사이의 거리, 이동 표현, 이동 횟수
# 1   1  1
# 2  1+1  2
# 3  1+1+1  3
# 4  1+2+1  3
# 이동 횟수만 뽑아보면, [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, ...]
