import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('input.txt', 'r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x: (x[1], x[0]))

for pair in a:
    print(' '.join(map(str,pair)))
