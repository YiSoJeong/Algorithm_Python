import sys
sys.stdin = open('sample_input.txt', 'r')

# sol 1
# 분류 : Brute Force
# 발상 : 이동할 수 있는 경우의 수 수열로 나열한 후 계산
# 변형 : 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량
# 조합 : 순열

# import itertools
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     battery = [list(map(int, input().split())) for _ in range(N)]
#     section = [i for i in range(1, N)]
#     ans = float('inf')
#     for path in list(itertools.permutations(section)):
#         total = 0
#         for i in range(N):
#             if i == 0:
#                 total += battery[0][path[i]]
#             elif i == N-1:
#                 total += battery[path[i-1]][0]
#             else:
#                 total += battery[path[i-1]][path[i]]
#         if total < ans:
#             ans = total
#
#     print('#{} {}'.format(t, ans))

# sol 2
# 분류 : Back Tracking
# 발상 : 각 구역을 모두 돌아야 함
# 변형 : 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량
# 조합 : dfs


def dfs(start):
    global total, ans
    if len(path) == N-1:
        for i, j in path:
            total += battery[i][j]
        total += battery[start][0]  # 마지막으로 방문한 구역
        if total < ans:
            ans = total
        total = 0
        return

    for next in range(1, N):
        if not visit[next]:
            path.append([start, next])
            visit[next] = True
            dfs(next)
            path.remove([start, next])
            visit[next] = False


T = int(input())
for t in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    visit = [False]*N
    path, total, ans = [], 0, float('inf')
    dfs(0)
    print('#{} {}'.format(t, ans))
