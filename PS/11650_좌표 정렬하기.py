import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

a.sort(key=lambda x: (x[0], x[1]))

for x in a:
    print(' '.join(map(str, x)))
