N = int(input())
arr = list(map(int, input().split()))
cnt = 0


def IsPrime(ele):
    if ele == 1: # 1은 소수가 아니다.
        return False
    for i in range(1, ele):
        if i == 1:
            continue
        elif ele % i == 0: # 1과 자기 자신 말고 나누어 떨어지는 수가 있으면
            return False # 소수가 아니다.
    return True


for ele in arr:
    if IsPrime(ele): # 소수이면 카운트
        # print(IsPrime(ele))
        cnt += 1

print(cnt)