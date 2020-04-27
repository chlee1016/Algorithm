import sys
n = int(input())
result = []
for i in range(n):
    ps = sys.stdin.readline().rstrip()
    lst = []
    for j in range(len(ps)):
        if len(lst) == 0:
            lst.append(ps[j])
        else:
            if lst[-1] == '(' and ps[j] == ')':
                lst.pop()
            else:
                lst.append(ps[j])
    # print(lst)
    if len(lst) == 0:
        result.append('YES')
    else:
        result.append('NO')

for i in range(n):
    print(result[i])

