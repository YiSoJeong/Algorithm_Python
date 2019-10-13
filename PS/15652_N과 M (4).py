import sys
from itertools import combinations_with_replacement as com

input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

for case in com(range(1, n+1), r=m):
    # print(*case) 76ms
    print(' '.join(map(str, case)))  # 68ms
