import sys
import queue
input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n = int(input())
q = queue.Queue()
for _ in range(n):
    op, *x = input().split()
    if op == 'push':
        q.put(x[0])
    elif op == 'pop':
        print(-1) if q.empty() else print(q.get())
    elif op == 'size':
        print(q.qsize())
    elif op == 'empty':
        print(1) if q.empty() else print(0)
    elif op == 'front':
        print(-1) if q.empty() else print(q.queue[0])
    elif op == 'back':
        print(-1) if q.empty() else print(q.queue[-1])

