li = []

for x in range(1,201):
    if x % 7 == 0 and x % 5 != 0:
        li.append(str(x))

print(','.join(li))
