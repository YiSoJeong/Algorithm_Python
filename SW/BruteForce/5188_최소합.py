import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Brute Force, 백트래킹
# 발상 : 출발 -> 도착으로 가는 방법 나열 후 덧셈, 탐색하면서 덧셈
# 변형 : 출발에서 도착까지 갈 때까지 지나는 칸의 합이 최소인 경우
# 조합 : 순열, dfs

# sol1 : 순열 만들어서 탐색 -> import itertools run error
# import itertools
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     dir = []
#     for _ in range(N-1):
#         dir.append([1, 0])
#         dir.append([0, 1])
#
#     ans = float('inf')
#     for path in list(itertools.permutations(dir)):
#         cur, cnt = [0, 0], arr[0][0]
#         for x in path:
#             cur[0] += x[0]
#             cur[1] += x[1]
#             cnt += arr[cur[0]][cur[1]]
#         if cnt < ans:
#             ans = cnt
#     print('#{} {}'.format(t, ans))

# sol2 : dfs, 백트래킹
dy = [0, 1]
dx = [1, 0]


def dfs(cur):
    global cnt, ans
    if cnt > ans:
        return

    if cur == [N-1, N-1]:
        if cnt < ans:
            ans = cnt
        return

    for i in range(2):
        ny = cur[0] + dy[i]
        nx = cur[1] + dx[i]
        if 0 <= ny < N and 0 <= nx < N and [ny, nx]:
            cnt += arr[ny][nx]
            dfs([ny, nx])
            cnt -= arr[ny][nx]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans, cnt = float('inf'), arr[0][0]
    dfs([0, 0])
    print('#{} {}'.format(t, ans))
