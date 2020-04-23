import sys
sys.stdin = open('sample_input.txt', 'r')

# 분류 : heap
# 발상 : 최소힙이라고 문제에 언급
# 변형 : 마지막 노드의 조상 노드에 저장된 값의 합
# 조합 : Priority Queue, Tree
# 참고 : https://www.daleseo.com/python-priority-queue/
#       https://www.daleseo.com/python-heapq/
import heapq

T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     heap = list(map(int, input().split()))
#     heapq.heapify(heap)
#     ans = 0
#     while N > 1:
#         N //= 2
#         print(N)
#         ans += heap[N-1]
#
#     print('#{} {}'.format(t, ans))

# root 안넣고 힙 만들 때
for t in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    heap, ans = [0, arr[1]], 0  # heap, ans = [0], 0

    for i in range(2, N+1):  # range(1, N+1)
        heap.append(arr[i])
        cur = i
        while cur > 1:  # while cur >= 1
            if heap[cur//2] > heap[cur]:
                heap[cur//2], heap[cur] = heap[cur], heap[cur//2]
            cur //= 2

    while N > 1:
        N //= 2
        ans += heap[N]

    print('#{} {}'.format(t, ans))
