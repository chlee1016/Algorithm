A, B, V = map(int, input().split())

if (V-B) % (A-B) == 0:
    day = (V-B) // (A-B)
else:
    day = (V-B) // (A-B) + 1

print(day)

# # 시간초과
# day = 1
# height = 0
# while True:
#     height += A
#     if height >= V:
#         print(day)
#         break
#     else:
#         height -= B

# 깨달은 것 : 부등식 문제 -> 굳이 for문 돌리지 않고
# if문으로 바로 해결하도록 먼저 시도해보기


