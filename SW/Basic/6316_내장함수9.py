even = list(filter(lambda x: x % 2 == 0, range(1, 11)))
square = list(map(lambda x: x*x, even))

print(square)
