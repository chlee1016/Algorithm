X = int(input())

k = 1
while True:
    if X > k:
        X -= k
        k += 1
    else: # 숫자가 있는 그룹으로 도착
        if k % 2 == 1: # k가 홀수이면
            nominator = k+1 - X
            denominator = k+1 - nominator
            print(nominator, end='')
            print("/", end='')
            print(denominator)
            break
        else: # k가 짝수이면
            nominator = X
            denominator = k+1 - nominator
            print(nominator, end='')
            print("/", end='')
            print(denominator)
            break


