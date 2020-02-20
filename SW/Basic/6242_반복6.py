blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a = b = o = ab = 0

for x in blood:
    if x == 'A':
        a += 1
    elif x == 'B':
        b += 1
    elif x == 'O':
        o += 1
    elif x == 'AB':
        ab += 1

print("{{'A': {}, 'O': {}, 'B': {}, 'AB': {}}}".format(a, o, b, ab))
