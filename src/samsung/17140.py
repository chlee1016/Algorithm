# 1. 행 연산, 열 연산 짜기
# 2. 조건문으로 열연산 행연산 구분짓기
# 3. 0패딩 넣기
# 4. 0패딩 반영하기
# 5. 행 또는 열의 크기가 100을 넘어가는 경우, 처음 100개만 취하기
# 런타임 에러 : if r < len(A) and c < len(A[0]) 이 조건을 안적어주어서
# transpose 하는 방법 list(map(list, zip(*a)))
# 리스트 기준 2개로 정렬하기

import copy


def calc(a):
    new_a = []
    key_lst = [0]  # 정렬할 때 0은 무시하기 위해 미리 넣어줌
    out = []
    for ele in a:
        if ele in key_lst:
            continue
        else:
            key_lst.append(ele)
            new_a.append([ele, a.count(ele)])
    new_a.sort(key=lambda x: (x[1], x[0]))
    # 등장횟수가 같은 것이 여러가지면 수가 커지는 순으로 정렬
    # 괄호 벗기고 append
    # [[3,1],[1,2]]
    # [3, 1, 1, 2]
    for ele_new_a in new_a:
        out.append(ele_new_a[0])
        out.append(ele_new_a[1])
    return out


def solve():
    r, c, k = map(int, input().split())
    r, c = r-1, c-1
    A = [list(map(int, input().split())) for _ in range(3)]
    sec = 0
    row_dim = 3
    col_dim = 3
    while True:
        if sec > 100:
            print(-1)
            break

        if r < len(A) and c < len(A[0]) and A[r][c] == k:
            print(sec)
            break

        else:
            sec += 1
            if row_dim >= col_dim:  # 행 >= 열 : 행연산
                temp_A = []
                for row in A:
                    calc_row = calc(row)
                    col_dim = max(col_dim, len(calc_row))
                    temp_A.append(calc_row)

                # 행 또는 열의 크기가 100 넘을때 앞의 100개만 취하기
                if col_dim > 100:
                    for row in temp_A:
                        while len(row) != 100:
                            row.pop()
                else:
                    # zero padding here
                    for row in temp_A:
                        if len(row) < col_dim:
                            for _ in range(col_dim - len(row)):
                                row.append(0)

                A = copy.deepcopy(temp_A)


            else:  # 행 < 열 : 열연산
                temp_B = []
                B = list(map(list, zip(*A)))
                for row in B:
                    calc_row = calc(row)
                    temp_B.append(calc_row)
                    row_dim = max(row_dim, len(calc_row))

                # 행 또는 열의 크기가 100 넘을때 앞의 100개만 취하기
                if row_dim > 100:
                    for row in temp_B:
                        while len(row) != 100:
                            row.pop()

                else:
                    # zero padding here
                    for row in temp_B:
                        if len(row) < row_dim:
                            for _ in range(row_dim - len(row)):
                                row.append(0)

                temp_B = list(map(list, zip(*temp_B)))  # transpose
                A = copy.deepcopy(temp_B)

solve()