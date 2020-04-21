import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : bfs
# 발상 : 탐색을 완료하는 데 걸리는 횟수
# 변형 : 미로를 탈출하는 데 이동하는 횟수
# 조합 : 2차원 배열 입력받기
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(cur):
    global cnt
    q.append(cur)

    while q:
        front = q.pop(0)
        for i in range(4):
            ny = front[0] + dy[i]
            nx = front[1] + dx[i]
            if (ny, nx) not in visit and 0 <= ny < N and 0 <= nx < N and (maze[ny][nx] == 0 or maze[ny][nx] == 3):
                visit.append((ny, nx))
                distance[ny][nx] = distance[front[0]][front[1]] + 1  # 이동했던 거리에 1추가
                q.append((ny, nx))
                if maze[ny][nx] == 3:
                    cnt = distance[ny][nx] - 1
                    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start = set()
    q, visit, cnt = [], [], 0
    distance = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
    bfs(start)
    print('#{} {}'.format(t, cnt))
