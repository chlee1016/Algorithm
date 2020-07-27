from collections import deque


def bfs(N, K):
    deq = deque()
    deq.append(N)
    sec = -1

    while deq:
        sec += 1
        for _ in range(len(deq)):
            N = deq.popleft()
            if N == K:
                return sec

            for nN in [N-1, N+1, N*2]:
                if -1 < nN < 100001 and visit[nN] == 0:
                    visit[nN] = 1
                    deq.append(nN)



N, K = map(int, input().split())
visit = [0]*100001

print(bfs(N, K))

# visit로 방문표시를 안해주어서 메모리초과가 뜸. 1차원이라고 이 부분을 간과하지 말자.




## 종료 조건을 하나로 합치기 전 코드
# from collections import deque
#
#
# def bfs(N, K):
#     deq = deque()
#
#     deq.append(N)
#     sec = 0
#     if N == K:
#         return sec
#
#     while deq:
#         sec += 1
#         for _ in range(len(deq)):
#             N = deq.popleft()
#
#             for nN in [N-1, N+1, N*2]:
#                 if -1 < nN < 100001 and visit[nN] == 0:
#                     if nN == K:
#                         return sec
#                     else:
#                         visit[nN] = 1
#                         deq.append(nN)
#
#
#
# N, K = map(int, input().split())
# visit = [0]*100001
#
# print(bfs(N, K))
#
# # visit로 방문표시를 안해주어서 메모리초과가 뜸. 1차원이라고 이 부분을 간과하지 말자.