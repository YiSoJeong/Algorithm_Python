import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : DFS
# 발상 : 트리 탐색
# 변형 : 노드간의 경로 존재 유뮤
# 조합 : 방향성 그래프


def dfs(tree, visit, start):
    stack = list()
    stack.append(start)
    visit[start] = True
    while stack:
        top = stack.pop(-1)
        if tree[top]:
            for x in tree[top]:
                stack.append(x)
                visit[x] = True


T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())
    tree = {i: set() for i in range(1, v+1)}
    visit = [False]*(v+1)
    ans = 0

    for _ in range(e):
        left, right = map(int, input().split())
        tree[left].add(right)

    start, end = map(int, input().split())
    dfs(tree, visit, start)

    if visit[end]:
        ans = 1
    print('#{} {}'.format(t,ans))
