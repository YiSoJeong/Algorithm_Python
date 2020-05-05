import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : MST
# 발상 : 사이클이 없는 최소신장트리 -> 크루스칼, 프림
# 변형 : 크루스칼 기본, 프림 기본
# 조합 : 상호배타 집합(유니온 파인드), 재귀, sort정렬 by key

# sol1 : 크루스칼
# def find_set(v):
#     if parent[v] == v:
#         return v
#     else:
#         return find_set(parent[v])
#
#
# def union(x, y):
#     parent[find_set(x)] = find_set(y)
#
#
# T = int(input())
# for t in range(1, T+1):
#     V, E = map(int, input().split())
#     parent = [i for i in range(V+1)]
#     G = []
#     mst, mst_cost = [], 0
#     for _ in range(E):
#         G.append(list(map(int, input().split())))
#     G.sort(key=lambda x: x[2])
#     while len(mst) < V:
#         start, end, weight = G.pop(0)
#         if find_set(start) != find_set(end):
#             union(start, end)
#             mst.append((start, end))
#             mst_cost += weight
#     print('#{} {}'.format(t, mst_cost))

# sol2 : 프림
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    visit = [False] * (V+1)
    key = [float('inf')] * (V+1)
    key[0] = 0

    G = {i: [] for i in range(V+1)}
    # 무향 그래프 -> 양쪽으로 연결필요
    for _ in range(E):
        start, end, weight = map(int, input().split())
        G[start].append((end, weight))
        G[end].append((start, weight))

    for _ in range(V+1):
        min = float('inf')
        minidx = -1
        for i in range(V+1):                    # 가중치가 최소인 정점 찾기
            if not visit[i] and key[i] < min:
                min = key[i]
                minidx = i
        visit[minidx] = True
        for v, weight in G[minidx]:             # 인접 정점의 가중치 갱신
            if not visit[v] and weight < key[v]:
                key[v] = weight
                parent[v] = minidx

    print('#{} {}'.format(t, sum(key)))
