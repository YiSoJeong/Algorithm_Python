fruit = ['   apple    ', 'banana', '  melon']
fruit = [x.strip() for x in fruit]

d = {x: len(x) for x in fruit}

print(d)
