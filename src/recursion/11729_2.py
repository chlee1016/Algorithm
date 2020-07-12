# https://www.youtube.com/watch?v=aPYE0anPZqI
# https://www.youtube.com/watch?v=aDcNywDHL_s

def hanoi(num, From, By, To):
    if num == 1:
        moves.append([From, To])
    else:
        hanoi(num-1, From, To, By)
        moves.append([From, To])
        hanoi(num-1, By, From, To)


n = int(input())
moves = []
hanoi(n, 1, 2, 3)
print(len(moves))
for move in moves:
    print(*move)

# * : Asterisk, unpacking