N = input()
iter_num = len(N)
N = int(N)


def disassemble_sum(N):  # 어떤 수를 넣었을때,
    # 그것의 분해합을 계산하는 함수
    global iter_num
    result = N
    for i in range(1, iter_num+1):
        result += (N % (10**i)) // 10**(i-1)
    return result

# 156
# 156%1000//100 -> 1
# 156%100//10 -> 5
# 156%10//1 -> 6
# result = 156 + 1 + 5 + 6


for k in range(1, N+1):
    if disassemble_sum(k) == N:
        print(k)
        break
else:
    print(0)

