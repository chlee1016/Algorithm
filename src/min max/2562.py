lst = []
for _ in range(9):
    lst.append(int(input().rstrip()))
print(max(lst))

for i in range(len(lst)):
    if lst[i] == max(lst):
        print(i+1)