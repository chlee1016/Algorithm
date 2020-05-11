# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = list(map(int, input().split()))

# solution 1
# from itertools import permutations
# p = permutations(range(1, n+1), m)
# for i in p:
#     # 이렇게 하면 m개 자릿수 만큼 출력을 하는 것이 아니어서 에러
#     # print(str(i[0]), end=' ')
#     # print(str(i[1]))
#
#     # join 함수는 함수 인자를 join 하되, ' '로 메꾸겠다는 것
#     print(' '.join(map(str, i)))


# solution 2
visited = [False] * n
out = []


def solve(depth, n, m):
    if depth == m:
        # 아래 한줄 코드와 같은 코드
        # for i in range(m):
        #    print(out[i], end=' ')
        # print()
        print(' '.join(map(str, out)))
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, n, m)
            visited[i] = False
            out.pop()

solve(0, n, m)
