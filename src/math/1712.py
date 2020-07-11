# A : 고정지출
# B : 노트북 한대 생산 비용
# C : 노트북 가격
# A + kB < kC
# 총 비용   총 수입
# 총 수입이 총 비용보다 많아지면 종료, k를 출력
A, B, C = map(int, input().split())

# 노트북 한대 생산 비용이 노트북 가격보다 같거나 크면
# 손익 분기점 발생 X
if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)


# while문으로 접근했을 때, 시간초과
# if B >= C:
#     print(-1)
# else:
#     k=1
#     while True:
#         if A + k*B < k*C:
#             print(k)
#             break
#         k += 1
#         if k == 210000001:
#             print(-1)
#             break
