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


