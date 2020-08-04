N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt_directors = []
for i in range(N):
    if A[i] <= B:  # 총 감독관으로 해결 가능한 경우
        cnt_directors.append(1)
    else:  # 총 감독관 + 부 감독관으로 해결 가능한 경우
        if (A[i]-B) % C == 0:
            cnt_directors.append(1 + (A[i]-B) // C)
        elif (A[i]-B) % C != 0:
            cnt_directors.append(1 + (A[i] - B) // C + 1)

print(sum(cnt_directors))
