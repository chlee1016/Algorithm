# 각 열에서 검사를 진행할 때, 가장 위에 있는 인형에 관해서 작업을 수행하고,
# break를 통해 탐색을 중지 해야한다.

def solution(board, moves):
    answer = 0
    bucket = []
    n = len(board)
    # 각 열의 스택마다 검사
    for i in moves:
        for j in range(n):
            # 각 열에서 가장 위에 있는 애들이면
            if board[j][i-1] != 0:
                # print(board[j][i-1])

                # 터트려져 사라진 인형의 개수
                if len(bucket) != 0 and bucket[-1] == board[j][i-1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[j][i - 1])
                board[j][i - 1] = 0
                break

    return answer



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = solution(board, moves)
print(answer)
# n=5
# for i in range(n):
#     print(board[i][0])