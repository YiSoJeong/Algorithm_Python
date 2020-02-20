li = []

for i in range(100, 301):
    s = str(i)
    isEven = True
    for x in s:
        if int(x) % 2 != 0:
            isEven = False
            break
    if isEven:
        li.append(s)

print(','.join(li))
