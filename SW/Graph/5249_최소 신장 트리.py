import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : MST 크루스칼
# 발상 : 사이클이 없는 최소신장트리 -> 크루스칼
# 변형 : 크루스칼 기본
# 조합 : 상호배타 집합(유니온 파인드), 재귀, sort정렬 by key


def find_set(v):
    if parent[v] == v:
        return v
    else:
        return find_set(parent[v])


def union(x, y):
    parent[find_set(x)] = find_set(y)


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    G = []
    mst, mst_cost = [], 0
    for _ in range(E):
        G.append(list(map(int, input().split())))
    G.sort(key=lambda x: x[2])
    while len(mst) < V:
        start, end, weight = G.pop(0)
        if find_set(start) != find_set(end):
            union(start, end)
            mst.append((start, end))
            mst_cost += weight
    print('#{} {}'.format(t, mst_cost))
