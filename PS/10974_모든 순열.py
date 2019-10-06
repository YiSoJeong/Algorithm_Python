from itertools import permutations

a = [i+1 for i in range(int(input()))]

for case in permutations(a):
    print(' '.join(map(str, case)))
