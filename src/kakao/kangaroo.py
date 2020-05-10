# 두마리의 캥거루가 있다.
# 이 캥거루들은 양의 방향으로 고정된 정수 크기만큼 점프를 할 수 있다.
# 캥거루들의 출발위치가 다르고 점프할 수 있는 크기가 다르다고 가정하자.
# 같은 횟수만큼 점프를 했을 때, 캥거루가 만나는 지점이 있는지 확인 하라.

# def kangaroo(x1, v1, x2, v2):
#     x1 = x1%v1
#     x2 = x2%v2
#     for i in range(int(v1*v2)):
#         if x1 + i * v1 == x2 + i * v2:
#             return 'YES'
#     return 'NO'


def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(result)

# Input : 0 3 4 2
# Output : YES

# Input : 0 2 5 3
# Output : NO


