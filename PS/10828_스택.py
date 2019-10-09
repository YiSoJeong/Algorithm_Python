import sys
input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n = int(input())
st = []
for _ in range(n):
    op, *x = input().split()
    if op == 'push':
        st.append(x[0])
    if op == 'pop':
        print(-1) if len(st) == 0 else print(st.pop())
    if op == 'size':
        print(len(st))
    if op == 'empty':
        print(1) if len(st) == 0 else print(0)
    if op == 'top':
        print(-1) if len(st) == 0 else print(st[-1])
