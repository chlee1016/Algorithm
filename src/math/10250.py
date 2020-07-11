# 나머지 계산의 특성상 꼭대기 층은 분리해서 연산해줘야 한다.
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        num_YY = H * 100
        num_XX = N // H
    else:
        num_YY = (N % H) * 100
        num_XX = N // H + 1

    print(num_YY + num_XX)