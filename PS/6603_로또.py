from itertools import combinations

while True:
    k, *S = map(int, input().split())

    if k == 0:
        break

    for case in combinations(S, 6):
        print(*case)
    print()
