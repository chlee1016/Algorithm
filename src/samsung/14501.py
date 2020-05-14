n = int(input())
# [0]*(n+1)과 [0]*n+1는 다름
t = []
p = []
max_pay = [0] * (n+1)  # list 초기화

for i in range(n):  # i는 0부터 6까지
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# t, p, dp 초기화 완료
# 끝에서부터 max_pay 값 갱신
for i in range(n-1, -1, -1):  # n-1, n-2, ..., 0까지
    # n번 반복
    # 마지막 날 상담부터 검사
    # 상담이 끝나는 날이 n을 넘어가면
    # i = 0이고, t[i] = 7, n= 7일 때에는 가능하니까 등호 포함
    # 즉, t[i] + i == n인 경우는 현재 일을 시작하고 정확히 마지막에 끝나는 경우

    if t[i] + i <= n:  # 일을 하게 되었을 때 기간이 지날 경우
        max_pay[i] = max(max_pay[i + 1], p[i] + max_pay[i + t[i]])
    else:  # 이전의 max 값을 가져온다 (일을 안하는 것, 값을 그대로 유지)
        max_pay[i] = max_pay[i + 1]

print(max_pay[0])

# 1) 현재 일의 이윤 + 현재 일에 필요한 day 이전의 이윤
# 2) 현재 일을 하지 않을 때의 이윤 (갱신 전인 i+1의 이윤)
# 1)과 2) 중 큰 값이 현재의 maximum pay
