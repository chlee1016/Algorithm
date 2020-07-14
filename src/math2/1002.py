T = int(input())
# 결국 이 문제는 원의 교점의 개수를 묻는 문제였음
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
        # 두 원이 만나지 않는 경우
        if dist > r1 + r2 or\
            max(r1, r2) > dist + min(r1, r2):
            print(0)
        # 두 원이 한점에서 만나는 경우 (외접하는 경우, 내접하는 경우)
        elif r1 + r2 == dist or\
            dist + min(r1, r2) == max(r1, r2):
            print(1)
        else:
            print(2)


