import sys
from itertools import combinations as com
input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for case in com(arr, m):
    print(' '.join(map(str, case)))
