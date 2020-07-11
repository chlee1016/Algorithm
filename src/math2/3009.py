x_lst = []
y_lst = []

for _ in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

ans_x = None
ans_y = None
for temp_x in x_lst:
    if x_lst.count(temp_x) == 1:
        ans_x = temp_x

for temp_y in y_lst:
    if y_lst.count(temp_y) == 1:
        ans_y = temp_y

print(ans_x, ans_y)
