import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : bfs
# 발상 : 인접 정점 탐색하기
# 변형 : 출발 노드에서 도착 노드까지 걸리는 간선의 수
# 조합 : queue


def bfs(cur):
    q.append(cur)
    visit[cur] = True

    while q:
        front = q.pop(0)
        for x in g[front]:
            if not visit[x]:
                q.append(x)
                visit[x] = True
                distance[x] = distance[front] + 1
                if x == end:
                    return
    return


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    g = {i: list() for i in range(1, V+1)}
    distance = [0]*(V+1)
    visit = [False]*(V+1)
    q = []
    for i in range(E):
        left, right = map(int, input().split())
        g[left].append(right)
        g[right].append(left)
    start, end = map(int, input().split())
    bfs(start)
    print('#{} {}'.format(t, distance[end]))
