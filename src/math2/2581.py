M = int(input())
N = int(input())
primes = []


def IsPrime(ele):
    if ele == 1:  # 1은 소수가 아니다.
        return False

    for i in range(1, ele):
        if i == 1:
            continue
        else:
            if ele % i == 0:  # 1과 자기 자신 외에 나누어 떨어지는 수가 있으면
                return False  # 소수가 아니다.
    # 나누어 떨어지는 수가 1과 자기 자신만 존재하면
    # True 리턴
    return True


for ele in range(M, N+1):
    if IsPrime(ele):
        primes.append(ele)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
