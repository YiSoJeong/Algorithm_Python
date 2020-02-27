a = [x for x in input().replace(' ','')]
let = d = 0

for x in a:
    if 'A' <= x <= 'z':
        let += 1
    elif '0' <= x <= '9':
        d += 1
    else:
        continue

print('LETTERS {}'.format(let))
print('DIGITS {}'.format(d))
