n, m = list(map(int, input().split()))
board = [list(input()) for i in range(n)]
# board = [list('BBBBBBBBWBWBW'), list('BBBBBBBBBWBWB'), list('BBBBBBBBWBWBW'), list('BBBBBBBBBWBWB'),
#          list('BBBBBBBBWBWBW'), list('BBBBBBBBBWBWB'), list('BBBBBBBBWBWBW'), list('BBBBBBBBBWBWB'),
#          list('WWWWWWWWWWBWB'), list('WWWWWWWWWWBWB')]

a = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
b = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]


def get_sliced_board(board, y, x):
    sliced_board = [[board[j+y][i+x] for i in range(8)] for j in range(8)]

    return sliced_board

def get_match_num(query, chess):
    match_num = 0
    for i in range(8):
        for j in range(8):
            if query[i][j] != chess[i][j]:
                match_num += 1
    return match_num


num_list = []
for y in range(n-8+1):
    for x in range(m-8+1):
        sliced_board = get_sliced_board(board, y, x)
        cnt = get_match_num(sliced_board, a)
        num_list.append(cnt)
        cnt = get_match_num(sliced_board, b)
        num_list.append(cnt)

print(min(num_list))

