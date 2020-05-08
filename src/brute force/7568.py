

def kangaroo(x1, v1, x2, v2):
    denom = int(min([v1, v2]))

    for i in range(int(v1*v2/denom)):
        if x1 + i * v1 == x2 + i * v2:
            return 'YES'
    return 'NO'

x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(type(result))
print(type('\n'))
print(result + '\n')

