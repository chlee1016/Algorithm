N = int(input())
A = list(map(int, input().split()))
opers_cnt = list(map(int, input().split()))
opers_dict = {0:'+', 1:'-', 2:'*', 3:'/'}


def calc(opers):
    result = A[0]
    for i in range(N-1):
        if opers[i] == '+':
            result += A[i+1]
        elif opers[i] == '-':
            result -= A[i+1]
        elif opers[i] == '*':
            result *= A[i+1]
        elif opers[i] == '/':
            if result < 0:
                result = -(-result // A[i+1])
            else:
                result //= A[i+1]

    return result



results = []
output = []

def solve(depth):
    if depth == N-1:  # depth 한 개가 늘어날 때마다,
        # operator 하나가 늘어나는 것이기 때문에
        # 종료 조건은 depth가 N-1일 때가 됨

        result = calc(output)
        results.append(result)
        return

    for i in range(4):
        if opers_cnt[i] != 0:
            opers_cnt[i] -= 1
            output.append(opers_dict[i])
            solve(depth+1)
            opers_cnt[i] += 1
            output.pop()


solve(0)


print(max(results))
print(min(results))


