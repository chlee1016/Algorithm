# 잘 생각해 보면 결국 각 행마다 하나의 퀸이 존재해야함


def isPromising(k, col):
    for row in range(1, k):
        if x[row] == col or abs(x[row]-col) == abs(row-k):
            return False
    return True


def nQueens(k): # k번째 행에 queen이 놓여질 수 있는지를 검사하는 함수
    global count
    for col in range(1, n+1): # k번째 행의 1번째 열부터 n번째 열까지 검사
        if isPromising(k, col) == True: # 조건을 만족하면 실행 (백트래킹 본질)
            x[k] = col # k번째 행의 열 정보를 저장
            if k < n: # 확장
                nQueens(k+1)
            else: # 확장 종료시 가능한 방법의 수를 의미하는 count 증가
                count += 1


count = 0
n = int(input())
x = [[0] * n for i in range(n+1)]
nQueens(1) # 1번째 행부터 검사
print(count)

# answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
# print(answer[int(input())])