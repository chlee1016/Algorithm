N = int(input())
# 미리 저장해둔 리스트로 시도하였으나 실패함
# lst = [666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669, 7666, 8666, 9666]
# print(((N-1) // 19)*10000 + lst[(N-1) % 19])

cnt = 0
num = 1  # 후보
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1
