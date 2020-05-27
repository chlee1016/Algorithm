#     1
#   1 0
#   1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
# 1<= n <= 10,000,000,000
n = 4
str_answer = []
answer_list = []
num = 0
while n > 0:
    str_answer.append(n % 2)
    n = n // 2
    # print(str_answer)

for i in range(len(str_answer)):
    if str_answer[i] == 1:
        num += 3 ** i
        answer_list.append(num)
# answer_list.sort()
# print(answer_list)