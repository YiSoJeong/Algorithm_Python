a = [12, 24, 35, 70, 88, 120, 155]
ret = [a[i] for i in range(len(a)) if i % 2 != 0]

print(ret)