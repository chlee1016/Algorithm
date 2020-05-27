# print(2016)
# print(2016//1000)
# print(2016 % 1000)
# print((2016//100) % 10)
# print((2016//10) % 100)
# print((2016//1) % 1000)

p = 2015
print(list(map(int, list(str(p)))))

for x in range(p+1, 10001):
    x_list = list(map(int, list(str(x))))
    if len(list(set(x_list))) == len(x_list):
        print(x)
        break
#     # print(x_list)
#     # print(len(list(set(x_list))))
#     print(len(x_list))

#     #     print(x_list)