import sys
from itertools import combinations as com

input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
no = [[0]*(n+1) for _ in range(n+1)]
cnt = 0

for i in range(m):
    x, y = map(int, input().split())
    no[x][y] = 1
    no[y][x] = 1

for case in com(range(1, n+1), 3):
    if no[case[0]][case[1]] or no[case[0]][case[2]] or no[case[1]][case[2]]:
        continue
    cnt += 1
print(cnt)
