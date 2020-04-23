import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Tree (중위 순회)
# 발상 : 이진 탐색 트리에서는 중위순회 -> 오름차순
# 변형 : 이진 탐색 트리에서 특정 노드 번호의 값 구하기
# 조합 : 재귀


def in_order(root):
    global val
    if root*2 <= N:
        in_order(root*2)
    tree[root] = val
    val += 1
    if root*2+1 <= N:
        in_order(root*2+1)
    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    val = 1
    in_order(1)
    print('#{} {} {}'.format(t, tree[1], tree[N//2]))
