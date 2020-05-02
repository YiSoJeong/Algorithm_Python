import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : 상호배타 집합
# 발상 : 그룹을 나누어 개수를 구하는 방법 -> 상호배타 집합의 수 구하기
# 변형 : 간선의 정보를 짝이 되고 싶은 사람을 적은 종이로 대체
# 조합 : recursion, set


def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


# 조금 더 최적화
# def link(x, y):
#     if rank[x] > rank[y]:
#         parent[y] = x
#     else:
#         parent[x] = y
#     if rank[x] == rank[y]:
#         rank[y] += 1


def union(x, y):
    # link(find_set(x), find_set(y))
    parent[find_set(y)] = find_set(x)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    relation = list(map(int, input().split()))
    parent = [x for x in range(N+1)]
    rank = [0]*(N+1)

    for i in range(0, len(relation), 2):
        union(relation[i], relation[i+1])

    s = set()
    for i in range(1, len(parent)):
        s.add(find_set(parent[i]))  # 자식의 모든 노드가 부모를 가르킬 수 있도록

    print('#{} {}'.format(t, len(s)))
