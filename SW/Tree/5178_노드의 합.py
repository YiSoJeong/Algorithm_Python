import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Tree (후위 순회)
# 발상 : 자식 노드의 합을 부모 노드에 저장 -> 자식부터 훑는 것 = 후위 순회
# 변형 : 부모 노드에 자식 노드의 합을 저장한 트리 만들기
# 조합 : 완전 이진 트리, 재귀, 트리 순회


def post_order(root):
    if root*2 > N:  # leaf 노드일 때
        return tree[root]
    left = post_order(root*2)
    if root*2+1 > N:  # 왼쪽 자식만 있을 때
        tree[root] = left
        return left
    right = post_order(root*2+1)
    tree[root] = left + right
    return left + right


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        leaf, val = map(int, input().split())
        tree[leaf] = val
    post_order(1)
    print('#{} {}'.format(t, tree[L]))
