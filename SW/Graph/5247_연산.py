import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : bfs
# 발상 : 가능한 연산이 4개 -> 트리구조로 찾아가면서 판단, dfs로 풀려고 했지만 재귀가 너무 많이 돌고 최소 횟수를 찾기 어려움
# 변형 : 이미 나왔던 자연수는 제외시켜서 중복된 숫자들 체크 방지 (가지치기)
# 조합 : 백트래킹, deque, lambda

from collections import deque  # deque(double-linked list기반): append, pop O(1)이지만 list에서는 O(n)
func = [lambda x:x+1, lambda x:x-1, lambda x:x*2, lambda x:x-10]


def bfs():
    global ans
    while Q:
        num, cnt = Q.popleft()
        if num == M:
            ans = cnt
            break
        for f in func:
            tmp = f(num)
            if 1 <= tmp <= 1000000 and not number[tmp]:
                Q.append((tmp, cnt+1))
                number[tmp] = True


T = int(input())
for t in range(1, T+1):
    number = [False]*1000001  # 이미 나왔던 숫자는 제외 -> 일종의 가지치기
    N, M = map(int, input().split())
    ans = 0
    Q = deque()
    Q.append((N, 0))
    # Q = [(N, 0)]
    number[N] = True
    bfs()
    print('#{} {}'.format(t, ans))
