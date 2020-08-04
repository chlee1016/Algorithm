import random
import time

dir_lst = [random.randint(0, 3) for _ in range(5000)]
dir_change_time = list(range(0, 10000, 2))

# 실험 1 :  if key in list 사용해서 검색할 경우
start_time = time.time()
direction = 0
sec = -1
iter_num = 0
while iter_num < 5000:
    iter_num += 1
    sec += 1
    if sec in dir_change_time:
        direction = dir_change_time[sec]
print('실험 1 소요 시간', time.time() - start_time)




dir_change_time = {}
for time, direction in zip(dir_change_time, dir_lst):
    dir_change_time[time] = direction


# 실험 2 :  if dir_change_time.get(sec) 사용해서 검색할 경우

start_time = time.time()
direction = 0
sec = -1
iter_num = 0
while iter_num < 5000:
    iter_num += 1
    sec += 1
    if dir_change_time.get(sec) is not None:
        direction = dir_change_time[sec]
print('실험 2 소요 시간', time.time() - start_time)

