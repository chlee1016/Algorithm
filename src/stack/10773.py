# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
# 이후 K개의 줄에 정수가 1개씩 주어진다.
# 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고,
# 아닐 경우 해당 수를 쓴다.
# 재민이가 최종적으로 적어 낸 수의 합을 출력한다.

k = int(input())
lst = []
for i in range(k):
    integer = int(input())
    if integer == 0:
        lst.pop()
    else:
        lst.append(integer)

print(sum(lst))

