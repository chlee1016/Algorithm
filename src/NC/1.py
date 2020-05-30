def solution(n):
    answer = 0
    n2 = n  # n 값 저장
    cnt_k = 0
    while(n!=0):
        cnt_k = cnt_k + n % 2
        n = n // 2

    n = n2
    for i in range(1, n):
        cnt = 0
        while(i!=0):
            cnt = cnt + i % 2
            i = i // 2

        if cnt_k == cnt:
            answer += 1

    return answer

answer = solution(9)
print(answer)
# expected result : 3

