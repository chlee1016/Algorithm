# 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면,
# 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
H, M = map(int, input().split())

if 60 * H + M - 45 < 0:
    alarm_time = 60 * H + M - 45 + 1440
    print(int(alarm_time / 60), alarm_time % 60)
else:
    alarm_time = 60 * H + M - 45
    print(int(alarm_time / 60), alarm_time % 60)
