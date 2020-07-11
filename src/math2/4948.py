def IsPrime(ele):
    if ele == 1:
        return False
    for i in range(2, int(ele**0.5)+1):
        if ele % i == 0:
            return False
    return True


while True:
    n = int(input())
    if n == 0:
        break
    else:
        primes = []

        for ele in range(n+1, 2*n + 1):
            if IsPrime(ele):
                primes.append(ele)
        print(len(primes))
