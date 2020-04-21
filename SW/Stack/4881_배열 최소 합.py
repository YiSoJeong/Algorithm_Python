import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 백트래킹
# 발상 : 안되는 경우가 있으면 되돌아 와야함
# 변형 : 가로세로가 안 겹치는 값들 합의 최소값
# 조합 : dfs


def dfs(y):
    global result, candidate
    if result < candidate:
        return

    if y == N:
        if candidate < result:
            result = candidate
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            candidate += arr[y][i]
            dfs(y+1)
            # return 못했으면 선택한 거 취소!
            visit[i] = False
            candidate -= arr[y][i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [False]*N
    candidate, result = 0, float('inf')
    dfs(0)
    print('#{} {}'.format(t, result))
