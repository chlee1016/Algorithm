# 재귀적인 패턴으로 별을 찍어 보자.
# N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
N = int(input())
matrix = [['*' for i in range(N)] for i in range(N)]


def star(N):
    if N % 3 == 0:
        for j in range(N//3):
            for i in range(N//3):
                matrix[N//3 + j][N//3 + i] = ' '
        star(N//3)


star(N)
for j in range(N):
    for i in range(N):
        print(matrix[j][i],end='')
    print('')






