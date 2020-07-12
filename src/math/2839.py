N = int(input())

# 5로만 커버 가능한 경우
if N % 5 == 0:
    print(N//5)

else:
    # for else문 : for문에서 break에 걸리지 않았을 때 else로 이동
    for a in range(N//5, -1, -1):
        # 5와 3으로 커버 가능한 경우
        if (N-5*a)%3 == 0:
            b = (N-5*a)//3
            print(a+b)
            break
    else:
        # 3으로만 커버 가능한 경우
        if N%3 == 0:
            print(N//3)
        else:
            print(-1)


