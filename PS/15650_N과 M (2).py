import sys
from itertools import combinations as com

input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

for case in list(com(list(range(1, n + 1)), m)):
    print(*case)
