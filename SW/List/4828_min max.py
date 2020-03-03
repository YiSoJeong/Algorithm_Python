import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(T):
    n = int(input())
    a = sorted(map(int, input().split(' ')))
    print('#{} {}'.format(t+1, a[n-1]-a[0]))
