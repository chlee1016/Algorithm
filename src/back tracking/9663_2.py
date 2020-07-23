N = int(input())
x = [0]*(N+1)  # idx 0는 사용안함


def isPromising(k, col):
    for row in range(1, k):  # k-1개의 행 검사,
        # range(0,k-1)로 할 경우, k=0이 입력되기 때문에 에러 발생
        if x[row] == col or abs(x[row]-col) == abs(row-k):
            return False
    return True


def nQueens(k):  # k번째 행을 검사하는 함수
    global count
    for col in range(1, N+1):  # N개의 열 후보군에 대해서 검사
        if isPromising(k, col):
            x[k] = col
            if k < N:
                nQueens(k+1)
            else:
                count += 1

count = 0
nQueens(1)  # 1번째 행부터 검사
print(count)
