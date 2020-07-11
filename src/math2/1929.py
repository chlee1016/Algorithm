# M, N = map(int, input().split())
#
# # 시간초과
# def IsPrime(ele):
#     if ele == 1:
#         return False
#     for i in range(1, ele):
#         if i == 1:
#             continue
#         else:
#             if ele % i == 0:
#                 return False
#     return True

M, N = map(int, input().split())

# 소수인지 검사할 때 2부터 i까지 검사하는 것이 아니라
# 2부터 i의 제곱근까지만 검사 -> 시간초과 해결
def IsPrime2(ele):
    if ele == 1:
        return False
    for i in range(2, int(ele**0.5)+1):
        if ele % i == 0:
            return False
    return True


for ele in range(M, N+1):
    if IsPrime2(ele):
        print(ele)


