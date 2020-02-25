from math import pi

r = list(map(int, input().split(', ')))

for i in range(len(r)):
    if i == len(r) - 1:
        print(round(2*pi*r[i], 2))
    else:
        print(round(2*pi*r[i], 2), end=', ')
