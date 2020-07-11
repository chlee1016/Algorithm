# 피타고라스 정리 이용해서 직각 삼각형인지 판단
def IsRight(a, b, c):
    if a**2 + b**2 == c**2 or\
        a**2 + c**2 == b**2 or\
        b**2 + c**2 == a**2:
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
