c = int(input())
for _ in range(c):
    seq = list(map(int, input().split()))
    n, scores = seq[0], seq[1:]
    avg = sum(scores) / n
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
    print("%.3f" % (cnt / n * 100) + "%")

# print함수로 출력할 문장(문자열)은 ' ' 또는 " " 로 감싸야 한다.
#
# 문자열 속에 ' 기호가 있는 경우에는 " "로
#
# “ 기호가 있는 경우에는 ' '를 사용하면 편리하게 출력할 수 있다.
#
# 콤마(,)로 문자열을 나열할 경우 공백(기본값)이 자동으로 추가 된다.
#
# 더하기(+) 기호로 문자열을 공백없이 연결할 수 있다.