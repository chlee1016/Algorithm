n = int(input())
num = list(map(int, input().split()))
oper_cnt = list(map(int, input().split()))


def get_oper_list(oper_cnt):
    oper_list = []
    for i in range(sum(oper_cnt)):
        if oper_cnt[0] != 0:
            oper_list.append('+')
            oper_cnt[0] -= 1
        elif oper_cnt[1] != 0:
            oper_list.append('-')
            oper_cnt[1] -= 1
        elif oper_cnt[2] != 0:
            oper_list.append('x')
            oper_cnt[2] -= 1
        elif oper_cnt[3] != 0:
            oper_list.append('/')
            oper_cnt[3] -= 1
    return oper_list

oper_list = get_oper_list(oper_cnt)
operation_set = []
from itertools import permutations
for opers in list(permutations(oper_list)):
    # if opers not in operation_set:
    operation_set.append(opers)
operation_set = list(set(operation_set))

min_result = 1000000001
max_result = -1000000001

for case in operation_set:
    result = num[0]
    for i in range(len(case)):

        if case[i] == '+':
            result += num[i+1]
        elif case[i] == '-':
            result -= num[i+1]
        elif case[i] == 'x':
            result *= num[i+1]
        elif case[i] == '/':
            if result < 0:
                result = -(-result // num[i+1])
            else:
                result = result // num[i+1]

    if result < min_result:
        min_result = result
    if result > max_result:
        max_result = result

print(max_result)
print(min_result)









