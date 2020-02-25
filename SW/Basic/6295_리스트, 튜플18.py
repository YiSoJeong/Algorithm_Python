row, col = map(int,input().split(', '))
m = []

for r in range(row):
    m.append([r * c for c in range(col)])

print(m)
