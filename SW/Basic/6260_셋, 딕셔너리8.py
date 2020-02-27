a = [x for x in input().replace(' ','')]
u = d = 0

for x in a:
    if 'A' <= x <= 'Z':
        u += 1
    elif 'a' <= x <= 'z':
        d += 1
    else:
        continue

print('UPPER CASE {}'.format(u))
print('LOWER CASE {}'.format(d))
