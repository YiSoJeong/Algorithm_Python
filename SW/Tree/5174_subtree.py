import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Tree
# 발상 : 서브트리를 순회
# 변형 : 서브트리의 순회하면서 노드 수 세기
# 조합 :


def pre_order(root):
    global cnt
    cnt += 1
    for x in tree[root]:
        pre_order(x)


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    tree = {i: list() for i in range(1, 1002)}
    links = list(map(int, input().split()))
    cnt = 0
    for i in range(E):
        par, chi = links[2*i], links[2*i+1]
        tree[par].append(chi)
    pre_order(N)
    print('#{} {}'.format(t, cnt))
