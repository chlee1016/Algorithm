# 1. 666
# 2. 1666
# 3. 2666
# 4. 3666
# 5. 4666
# 6. 5666
# 7. 6660
# 8. 6661
# 9. 6662
n = int(input())
cnt = 0
number = 0
while True:
    number += 1
    if '666' in str(number):
        cnt += 1
    if cnt == n:
        print(number)
        break

