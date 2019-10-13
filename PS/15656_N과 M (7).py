import sys
from itertools import product

input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for case in product(arr, repeat=m):
    # print(*case)  # 2332ms
    print(' '.join(map(str, case)))  # 1728ms
