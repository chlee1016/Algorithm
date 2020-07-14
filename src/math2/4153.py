# 피타고라스 정리 이용해서 직각 삼각형인지 판단
# Sort 반영하면 한 문장으로 가능
def IsRight(a, b, c):
    a, b, c = sorted([a, b, c])
    if a**2 + b**2 == c**2:
        return True

    return False


while True:
    a, b, c = map(int, input().split())
    if [a, b, c] == [0, 0, 0]:
        break
    else:
        if IsRight(a, b, c):
            print('right')
        else:
            print('wrong')
