a = [12, 24, 35, 70, 88, 120, 155]
result = [a[i] for i in range(len(a)) if i != 0 if i != 4 if i != 5]
# result = [a[i] for i in range(len(a)) if i != 0 and i != 4 and i != 5]

print(result)
