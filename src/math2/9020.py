T = int(input())


def IsPrime(ele):
    if ele == 1:
        return False
    else:
        for i in range(2, int(ele**0.5)+1):
            if ele % i == 0:
                return False
    return True


for _ in range(T):
    n = int(input())
    num1, num2 = None, None
    for k in range(1, n//2+1):  # num1, num2 자리 바꾸어도 같은 경우가 나오므로 계산량 줄임
        if IsPrime(k):
            if IsPrime(n-k):
                num1 = k
                num2 = n-num1

    print(num1, num2)
