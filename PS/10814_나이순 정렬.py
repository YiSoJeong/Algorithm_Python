import sys
input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n = int(input())
a = [input().split() for _ in range(n)]

a.sort(key=lambda x: int(x[0]))

for case in a:
    print(' '.join(map(str, case)))
