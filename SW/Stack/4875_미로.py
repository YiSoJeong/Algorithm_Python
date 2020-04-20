import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 백트래킹
# 발상 : 출발지에서 도착지까지 도착하는 경로가 존재하는 지 판단 (decision)
# 변형 : 미로에서 나갈 수 있는 지
# 조합 : dfs

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 0 : 통로,  1 : 벽, 2 : 출발, 3 : 도착
def dfs(cur):
    global ans

    visit.append(cur)
    for i in range(4):
        ny = cur[0]+dy[i]
        nx = cur[1]+dx[i]
        if 0 <= ny < n and 0 <= nx < n and (maze[ny][nx] == 0 or maze[ny][nx] == 3) and (ny, nx) not in visit:
            if maze[ny][nx] == 3:
                ans = 1
                return
            else:
                dfs((ny, nx))


T = int(input())
for t in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visit = []
    start, end = set(), set()
    ans = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    if not start or not end:
        ans = 'error'
    else:
        dfs(start)

    print('#{} {}'.format(t, ans))
