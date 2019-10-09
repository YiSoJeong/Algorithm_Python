import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n = int(input())
dq = deque()
for _ in range(n):
    op, *x = input().split()
    if op == 'push_front':
        dq.appendleft(x[0])
    if op == 'push_back':
        dq.append(x[0])
    if op == 'pop_front':
        print(-1) if len(dq) == 0 else print(dq.popleft())
    if op == 'pop_back':
        print(-1) if len(dq) == 0 else print(dq.pop())
    if op == 'size':
        print(len(dq))
    if op == 'empty':
        print(1) if len(dq) == 0 else print(0)
    if op == 'front':
        print(-1) if len(dq) == 0 else print(dq[0])
    if op == 'back':
        print(-1) if len(dq) == 0 else print(dq[-1])
