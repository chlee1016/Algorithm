N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

superviser_num = 0
x = 0

for i in range(len(A)):
    # 총감독관 혼자서 감독이 가능한 경우
    if A[i]-B <= 0:
        x = 0
    # 부감독관이 감시해야할 학생 수가 딱 나누어 떨어지는 경우
    elif (A[i]-B) % C == 0:
        x = (A[i]-B) // C
    # 그렇지 않은 경우, 부감독관의 수는 (학생수/C)의 몫 + 1이 된다.
    else:
        x = ((A[i]-B)//C) + 1
    superviser_num += (1 + x)

print(superviser_num)



