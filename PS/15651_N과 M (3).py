import sys
from itertools import product
input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

for case in product(range(1, n+1), repeat=m):
    # print(*case) 2044ms
    print(' '.join(map(str, case))) # 1556ms
