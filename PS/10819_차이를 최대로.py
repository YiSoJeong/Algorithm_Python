import sys
from itertools import permutations as pm

input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n = int(input())
a = list(map(int, input().split()))
Max = 0

for case in pm(a):
    total = 0
    for i in range(n-1):
        total += abs(case[i]-case[i+1])
    Max = max(Max, total)

print(Max)
