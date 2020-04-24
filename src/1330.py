# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
