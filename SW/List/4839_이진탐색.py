import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : Binary Search
# 발상 : 문제에 대놓고 이진탐색이라고 알려줌
# 변형 : 두 사람이 각각 이진탐색을 수행하고 걸린 시간 비교, 문제에서 idx 수정 알려줌
# 조합 : 구현


def binary_search(p, key):
    s = 1
    e = p
    cnt = 0
    while s <= e:
        cnt += 1
        m = (s + e) // 2
        if m == key:
            break
        elif m > key:
            e = m
        elif m < key:
            s = m
    return cnt


T = int(input())
for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    winner = 0
    if binary_search(P, Pa) < binary_search(P, Pb):
        winner = 'A'
    elif binary_search(P, Pb) < binary_search(P, Pa):
        winner = 'B'
    print('#{} {}'.format(t, winner))
